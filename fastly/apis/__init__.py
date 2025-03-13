
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from fastly.api.acl_api import AclApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from fastly.api.acl_api import AclApi
from fastly.api.acl_entry_api import AclEntryApi
from fastly.api.acls_in_compute_api import AclsInComputeApi
from fastly.api.apex_redirect_api import ApexRedirectApi
from fastly.api.automation_tokens_api import AutomationTokensApi
from fastly.api.backend_api import BackendApi
from fastly.api.billing_address_api import BillingAddressApi
from fastly.api.billing_invoices_api import BillingInvoicesApi
from fastly.api.billing_usage_metrics_api import BillingUsageMetricsApi
from fastly.api.cache_settings_api import CacheSettingsApi
from fastly.api.condition_api import ConditionApi
from fastly.api.config_store_api import ConfigStoreApi
from fastly.api.config_store_item_api import ConfigStoreItemApi
from fastly.api.contact_api import ContactApi
from fastly.api.content_api import ContentApi
from fastly.api.customer_api import CustomerApi
from fastly.api.customer_addresses_api import CustomerAddressesApi
from fastly.api.dictionary_api import DictionaryApi
from fastly.api.dictionary_info_api import DictionaryInfoApi
from fastly.api.dictionary_item_api import DictionaryItemApi
from fastly.api.diff_api import DiffApi
from fastly.api.director_api import DirectorApi
from fastly.api.director_backend_api import DirectorBackendApi
from fastly.api.domain_api import DomainApi
from fastly.api.domain_inspector_historical_api import DomainInspectorHistoricalApi
from fastly.api.domain_inspector_realtime_api import DomainInspectorRealtimeApi
from fastly.api.domain_ownerships_api import DomainOwnershipsApi
from fastly.api.events_api import EventsApi
from fastly.api.gzip_api import GzipApi
from fastly.api.header_api import HeaderApi
from fastly.api.healthcheck_api import HealthcheckApi
from fastly.api.historical_api import HistoricalApi
from fastly.api.http3_api import Http3Api
from fastly.api.iam_permissions_api import IamPermissionsApi
from fastly.api.iam_roles_api import IamRolesApi
from fastly.api.iam_service_groups_api import IamServiceGroupsApi
from fastly.api.iam_user_groups_api import IamUserGroupsApi
from fastly.api.image_optimizer_default_settings_api import ImageOptimizerDefaultSettingsApi
from fastly.api.insights_api import InsightsApi
from fastly.api.invitations_api import InvitationsApi
from fastly.api.kv_store_api import KvStoreApi
from fastly.api.kv_store_item_api import KvStoreItemApi
from fastly.api.log_explorer_api import LogExplorerApi
from fastly.api.logging_azureblob_api import LoggingAzureblobApi
from fastly.api.logging_bigquery_api import LoggingBigqueryApi
from fastly.api.logging_cloudfiles_api import LoggingCloudfilesApi
from fastly.api.logging_datadog_api import LoggingDatadogApi
from fastly.api.logging_digitalocean_api import LoggingDigitaloceanApi
from fastly.api.logging_elasticsearch_api import LoggingElasticsearchApi
from fastly.api.logging_ftp_api import LoggingFtpApi
from fastly.api.logging_gcs_api import LoggingGcsApi
from fastly.api.logging_grafanacloudlogs_api import LoggingGrafanacloudlogsApi
from fastly.api.logging_heroku_api import LoggingHerokuApi
from fastly.api.logging_honeycomb_api import LoggingHoneycombApi
from fastly.api.logging_https_api import LoggingHttpsApi
from fastly.api.logging_kafka_api import LoggingKafkaApi
from fastly.api.logging_kinesis_api import LoggingKinesisApi
from fastly.api.logging_logentries_api import LoggingLogentriesApi
from fastly.api.logging_loggly_api import LoggingLogglyApi
from fastly.api.logging_logshuttle_api import LoggingLogshuttleApi
from fastly.api.logging_newrelic_api import LoggingNewrelicApi
from fastly.api.logging_newrelicotlp_api import LoggingNewrelicotlpApi
from fastly.api.logging_openstack_api import LoggingOpenstackApi
from fastly.api.logging_papertrail_api import LoggingPapertrailApi
from fastly.api.logging_pubsub_api import LoggingPubsubApi
from fastly.api.logging_s3_api import LoggingS3Api
from fastly.api.logging_scalyr_api import LoggingScalyrApi
from fastly.api.logging_sftp_api import LoggingSftpApi
from fastly.api.logging_splunk_api import LoggingSplunkApi
from fastly.api.logging_sumologic_api import LoggingSumologicApi
from fastly.api.logging_syslog_api import LoggingSyslogApi
from fastly.api.mutual_authentication_api import MutualAuthenticationApi
from fastly.api.object_storage_access_keys_api import ObjectStorageAccessKeysApi
from fastly.api.observability_custom_dashboards_api import ObservabilityCustomDashboardsApi
from fastly.api.origin_inspector_historical_api import OriginInspectorHistoricalApi
from fastly.api.origin_inspector_realtime_api import OriginInspectorRealtimeApi
from fastly.api.package_api import PackageApi
from fastly.api.pool_api import PoolApi
from fastly.api.pop_api import PopApi
from fastly.api.product_ai_accelerator_api import ProductAiAcceleratorApi
from fastly.api.product_bot_management_api import ProductBotManagementApi
from fastly.api.product_brotli_compression_api import ProductBrotliCompressionApi
from fastly.api.product_ddos_protection_api import ProductDdosProtectionApi
from fastly.api.product_domain_inspector_api import ProductDomainInspectorApi
from fastly.api.product_fanout_api import ProductFanoutApi
from fastly.api.product_image_optimizer_api import ProductImageOptimizerApi
from fastly.api.product_log_explorer_insights_api import ProductLogExplorerInsightsApi
from fastly.api.product_ngwaf_api import ProductNgwafApi
from fastly.api.product_object_storage_api import ProductObjectStorageApi
from fastly.api.product_origin_inspector_api import ProductOriginInspectorApi
from fastly.api.product_websockets_api import ProductWebsocketsApi
from fastly.api.public_ip_list_api import PublicIpListApi
from fastly.api.publish_api import PublishApi
from fastly.api.purge_api import PurgeApi
from fastly.api.rate_limiter_api import RateLimiterApi
from fastly.api.realtime_api import RealtimeApi
from fastly.api.request_settings_api import RequestSettingsApi
from fastly.api.resource_api import ResourceApi
from fastly.api.response_object_api import ResponseObjectApi
from fastly.api.secret_store_api import SecretStoreApi
from fastly.api.secret_store_item_api import SecretStoreItemApi
from fastly.api.server_api import ServerApi
from fastly.api.service_api import ServiceApi
from fastly.api.service_authorizations_api import ServiceAuthorizationsApi
from fastly.api.settings_api import SettingsApi
from fastly.api.snippet_api import SnippetApi
from fastly.api.star_api import StarApi
from fastly.api.stats_api import StatsApi
from fastly.api.sudo_api import SudoApi
from fastly.api.tls_activations_api import TlsActivationsApi
from fastly.api.tls_bulk_certificates_api import TlsBulkCertificatesApi
from fastly.api.tls_certificates_api import TlsCertificatesApi
from fastly.api.tls_configurations_api import TlsConfigurationsApi
from fastly.api.tls_csrs_api import TlsCsrsApi
from fastly.api.tls_domains_api import TlsDomainsApi
from fastly.api.tls_private_keys_api import TlsPrivateKeysApi
from fastly.api.tls_subscriptions_api import TlsSubscriptionsApi
from fastly.api.tokens_api import TokensApi
from fastly.api.user_api import UserApi
from fastly.api.vcl_api import VclApi
from fastly.api.vcl_diff_api import VclDiffApi
from fastly.api.version_api import VersionApi
from fastly.api.waf_active_rules_api import WafActiveRulesApi
from fastly.api.waf_exclusions_api import WafExclusionsApi
from fastly.api.waf_firewall_versions_api import WafFirewallVersionsApi
from fastly.api.waf_firewalls_api import WafFirewallsApi
from fastly.api.waf_rule_revisions_api import WafRuleRevisionsApi
from fastly.api.waf_rules_api import WafRulesApi
from fastly.api.waf_tags_api import WafTagsApi
from fastly.api.whole_platform_ddos_historical_api import WholePlatformDdosHistoricalApi
