"""
fastly - Fastly Command Line Utility
"""

import os
import argparse

import fastly

from _version import __version__ as fastly_version

api = fastly.API()


def main():
    # Process command line arguments
    argparser = argparse.ArgumentParser(
        description=__doc__,
        epilog="FASTLY_KEY environment variable will be consulted if not provided as a parameter."
    )

    argparser.add_argument(
        "-k", "--fastly-key", required=False,
        help="Fastly key", default=os.environ.get('FASTLY_KEY')
    )

    argparser.add_argument(
        "--version",
        action="version", version="%(prog)s {}".format(fastly_version)
    )

    commands = argparser.add_subparsers(
        title='commands',
        help='action',
        dest='command',
    )

    # These parsers are used multiple times
    service_parser = argparse.ArgumentParser(add_help=False)
    service_parser.add_argument(
        'service_id',
        help='Service ID',
    )

    version_parser = argparse.ArgumentParser(add_help=False)
    version_parser.add_argument(
        'version_id',
        type=int,
        help='Version ID',
    )

    vcl_parser = argparse.ArgumentParser(add_help=False)
    vcl_parser.add_argument(
        'vcl_name',
        help='VCL Name',
    )

    # Add commands
    parser_services = commands.add_parser(
        "services",
        help="list services",
    ).set_defaults(cmd=cmd_services)

    parser_service = commands.add_parser(
        "service",
        help="service details",

        parents=[service_parser],
    ).set_defaults(cmd=cmd_service)

    parser_service = commands.add_parser(
        "purge_service",
        help="purge entire service",

        parents=[service_parser],
    ).set_defaults(cmd=cmd_purge_service)

    parser_versions = commands.add_parser(
        "versions",
        help="list versions",

        parents=[service_parser],
    ).set_defaults(cmd=cmd_versions)

    parser_version = commands.add_parser(
        "version",
        help="version info",

        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_version)

    parser_version = commands.add_parser(
        "newversion",
        help="create a brand new version",

        parents=[service_parser],
    ).set_defaults(cmd=cmd_newversion)

    parser_activate = commands.add_parser(
        "activate",
        help="activate version",
        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_activate)

    parser_deactivate = commands.add_parser(
        "deactivate",
        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_deactivate)

    parser_clone = commands.add_parser(
        "clone",
        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_clone)

    parser_lock = commands.add_parser(
        "lock",
        help="lock version",
        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_lock)

    parser_boilerplate = commands.add_parser(
        "boilerplate",
        help="boilerplate?",
        parents=[service_parser, version_parser],
    )
    parser_boilerplate.set_defaults(cmd=cmd_boilerplate)
    parser_boilerplate.add_argument(
        "file",
        nargs="?", default="-", type=argparse.FileType('w')
    )

    parser_lock = commands.add_parser(
        "generated_vcl",
        help="generated_vcl?",
        parents=[service_parser, version_parser],
    ).set_defaults(cmd=cmd_generated_vcl)

    parser_backends = commands.add_parser(
        "backends",
        help="list backends",

        parents=[service_parser, version_parser]
    )
    parser_backends.set_defaults(cmd=cmd_backends)

    parser_vcls = commands.add_parser(
        "vcls",
        help="list vcls",

        parents=[service_parser, version_parser]
    ).set_defaults(cmd=cmd_vcls)

    parser_vcl = commands.add_parser(
        "vcl",
        help="vcl details",

        parents=[service_parser, version_parser, vcl_parser]
    )
    parser_vcl.set_defaults(cmd=cmd_vcl)

    parser_main = commands.add_parser(
        "main",
        help="set VCL to be main",

        parents=[service_parser, version_parser, vcl_parser]
    )
    parser_main.set_defaults(cmd=cmd_main)

    parser_download = commands.add_parser(
        "download",
        help="download VCL",

        parents=[service_parser, version_parser, vcl_parser]
    )
    parser_download.set_defaults(cmd=cmd_download)
    parser_download.add_argument(
        "file",
        nargs="?", default="-", type=argparse.FileType('w')
    )

    parser_upload = commands.add_parser(
        "upload",
        help="upload VCL",

        parents=[service_parser, version_parser, vcl_parser]
    )
    parser_upload.set_defaults(cmd=cmd_upload)
    parser_upload.add_argument(
        "file",
        nargs="?", default="-", type=argparse.FileType('r')
    )

    parser_domains = commands.add_parser(
        "domains",
        help="list domains",

        parents=[service_parser, version_parser]
    ).set_defaults(cmd=cmd_domains)

    # Now actually parse the arguments, log into the API, and run the command
    args = argparser.parse_args()
    api.authenticate_by_key(args.fastly_key)
    args.cmd(args)


# Services Commands
def cmd_services(args):
    for service in api.services():
        print "{name} [{id}]".format(**service.attrs)


def cmd_service(args):
    print api.service(args.service_id).attrs


def cmd_purge_service(args):
    print api.service(args.service_id).purge_all()


def cmd_newversion(args):
    print api.service(args.service_id).version()


# Version Commands
def cmd_versions(args):
    version_line = "{is_active}{number} {created_at}/{updated_at} [{comment}]"
    for version in api.versions(args.service_id):
        print version_line.format(
            is_active=('*' if version.attrs['active'] else ' '),
            **version.attrs
        )


def cmd_version(args):
    version = api.version(args.service_id, args.version_id)
    print version.attrs


def cmd_activate(args):
    version = api.version(args.service_id, args.version_id)
    print version.activate()


def cmd_clone(args):
    version = api.version(args.service_id, args.version_id)
    print version.clone()


def cmd_deactivate(args):
    version = api.version(args.service_id, args.version_id)
    print version.deactivate()


def cmd_lock(args):
    version = api.version(args.service_id, args.version_id)
    print version.lock()


def cmd_boilerplate(args):
    version = api.version(args.service_id, args.version_id)
    args.file.write(version.boilerplate())


def cmd_generated_vcl(args):
    version = api.version(args.service_id, args.version_id)
    print version.generated_vcl()


# Backend Commands
def cmd_backends(args):
    for backend in api.backends(args.service_id, args.version_id):
        print backend.attrs


# VCL Commands
def cmd_vcls(args):
    vcl_line = "# {name}{is_main} {created_at}/{updated_at}\n\n{content}"
    for vcl in api.vcls(args.service_id, args.version_id):
        print vcl_line.format(
            is_main=('*' if vcl.attrs['main'] else ' '),
            **vcl.attrs
        )


def cmd_vcl(args):
    vcl = api.vcl(args.service_id, args.version_id, args.vcl_name)
    print vcl.attrs


def cmd_main(args):
    vcl = api.vcl(args.service_id, args.version_id, args.vcl_name)
    print vcl.main()


def cmd_download(args):
    vcl = api.vcl(args.service_id, args.version_id, args.vcl_name)
    args.file.write(vcl.download())


def cmd_upload(args):
    try:
        vcl = api.vcl(args.service_id, args.version_id, args.vcl_name)

        vcl.attrs['content'] = args.file.read()
        vcl.save()

        print vcl.attrs

    except Exception:
        ver = api.version(args.service_id, args.version_id)

        vcl = ver.vcl(args.vcl_name, args.file.read())

        print vcl.attrs


# Domain Commands
def cmd_domains(args):
    for domain in api.domains(args.service_id, args.version_id):
        # print domain
        print "{name} [{comment}]".format(**domain.attrs)
