# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: release-1.16
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.core_v1_api import CoreV1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCoreV1Api(unittest.TestCase):
    """CoreV1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.core_v1_api.CoreV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_connect_delete_namespaced_pod_proxy(self):
        """Test case for connect_delete_namespaced_pod_proxy

        """
        pass

    def test_connect_delete_namespaced_pod_proxy_with_path(self):
        """Test case for connect_delete_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_delete_namespaced_service_proxy(self):
        """Test case for connect_delete_namespaced_service_proxy

        """
        pass

    def test_connect_delete_namespaced_service_proxy_with_path(self):
        """Test case for connect_delete_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_delete_node_proxy(self):
        """Test case for connect_delete_node_proxy

        """
        pass

    def test_connect_delete_node_proxy_with_path(self):
        """Test case for connect_delete_node_proxy_with_path

        """
        pass

    def test_connect_get_namespaced_pod_attach(self):
        """Test case for connect_get_namespaced_pod_attach

        """
        pass

    def test_connect_get_namespaced_pod_exec(self):
        """Test case for connect_get_namespaced_pod_exec

        """
        pass

    def test_connect_get_namespaced_pod_portforward(self):
        """Test case for connect_get_namespaced_pod_portforward

        """
        pass

    def test_connect_get_namespaced_pod_proxy(self):
        """Test case for connect_get_namespaced_pod_proxy

        """
        pass

    def test_connect_get_namespaced_pod_proxy_with_path(self):
        """Test case for connect_get_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_get_namespaced_service_proxy(self):
        """Test case for connect_get_namespaced_service_proxy

        """
        pass

    def test_connect_get_namespaced_service_proxy_with_path(self):
        """Test case for connect_get_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_get_node_proxy(self):
        """Test case for connect_get_node_proxy

        """
        pass

    def test_connect_get_node_proxy_with_path(self):
        """Test case for connect_get_node_proxy_with_path

        """
        pass

    def test_connect_head_namespaced_pod_proxy(self):
        """Test case for connect_head_namespaced_pod_proxy

        """
        pass

    def test_connect_head_namespaced_pod_proxy_with_path(self):
        """Test case for connect_head_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_head_namespaced_service_proxy(self):
        """Test case for connect_head_namespaced_service_proxy

        """
        pass

    def test_connect_head_namespaced_service_proxy_with_path(self):
        """Test case for connect_head_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_head_node_proxy(self):
        """Test case for connect_head_node_proxy

        """
        pass

    def test_connect_head_node_proxy_with_path(self):
        """Test case for connect_head_node_proxy_with_path

        """
        pass

    def test_connect_options_namespaced_pod_proxy(self):
        """Test case for connect_options_namespaced_pod_proxy

        """
        pass

    def test_connect_options_namespaced_pod_proxy_with_path(self):
        """Test case for connect_options_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_options_namespaced_service_proxy(self):
        """Test case for connect_options_namespaced_service_proxy

        """
        pass

    def test_connect_options_namespaced_service_proxy_with_path(self):
        """Test case for connect_options_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_options_node_proxy(self):
        """Test case for connect_options_node_proxy

        """
        pass

    def test_connect_options_node_proxy_with_path(self):
        """Test case for connect_options_node_proxy_with_path

        """
        pass

    def test_connect_patch_namespaced_pod_proxy(self):
        """Test case for connect_patch_namespaced_pod_proxy

        """
        pass

    def test_connect_patch_namespaced_pod_proxy_with_path(self):
        """Test case for connect_patch_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_patch_namespaced_service_proxy(self):
        """Test case for connect_patch_namespaced_service_proxy

        """
        pass

    def test_connect_patch_namespaced_service_proxy_with_path(self):
        """Test case for connect_patch_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_patch_node_proxy(self):
        """Test case for connect_patch_node_proxy

        """
        pass

    def test_connect_patch_node_proxy_with_path(self):
        """Test case for connect_patch_node_proxy_with_path

        """
        pass

    def test_connect_post_namespaced_pod_attach(self):
        """Test case for connect_post_namespaced_pod_attach

        """
        pass

    def test_connect_post_namespaced_pod_exec(self):
        """Test case for connect_post_namespaced_pod_exec

        """
        pass

    def test_connect_post_namespaced_pod_portforward(self):
        """Test case for connect_post_namespaced_pod_portforward

        """
        pass

    def test_connect_post_namespaced_pod_proxy(self):
        """Test case for connect_post_namespaced_pod_proxy

        """
        pass

    def test_connect_post_namespaced_pod_proxy_with_path(self):
        """Test case for connect_post_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_post_namespaced_service_proxy(self):
        """Test case for connect_post_namespaced_service_proxy

        """
        pass

    def test_connect_post_namespaced_service_proxy_with_path(self):
        """Test case for connect_post_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_post_node_proxy(self):
        """Test case for connect_post_node_proxy

        """
        pass

    def test_connect_post_node_proxy_with_path(self):
        """Test case for connect_post_node_proxy_with_path

        """
        pass

    def test_connect_put_namespaced_pod_proxy(self):
        """Test case for connect_put_namespaced_pod_proxy

        """
        pass

    def test_connect_put_namespaced_pod_proxy_with_path(self):
        """Test case for connect_put_namespaced_pod_proxy_with_path

        """
        pass

    def test_connect_put_namespaced_service_proxy(self):
        """Test case for connect_put_namespaced_service_proxy

        """
        pass

    def test_connect_put_namespaced_service_proxy_with_path(self):
        """Test case for connect_put_namespaced_service_proxy_with_path

        """
        pass

    def test_connect_put_node_proxy(self):
        """Test case for connect_put_node_proxy

        """
        pass

    def test_connect_put_node_proxy_with_path(self):
        """Test case for connect_put_node_proxy_with_path

        """
        pass

    def test_create_namespace(self):
        """Test case for create_namespace

        """
        pass

    def test_create_namespaced_binding(self):
        """Test case for create_namespaced_binding

        """
        pass

    def test_create_namespaced_config_map(self):
        """Test case for create_namespaced_config_map

        """
        pass

    def test_create_namespaced_endpoints(self):
        """Test case for create_namespaced_endpoints

        """
        pass

    def test_create_namespaced_event(self):
        """Test case for create_namespaced_event

        """
        pass

    def test_create_namespaced_limit_range(self):
        """Test case for create_namespaced_limit_range

        """
        pass

    def test_create_namespaced_persistent_volume_claim(self):
        """Test case for create_namespaced_persistent_volume_claim

        """
        pass

    def test_create_namespaced_pod(self):
        """Test case for create_namespaced_pod

        """
        pass

    def test_create_namespaced_pod_binding(self):
        """Test case for create_namespaced_pod_binding

        """
        pass

    def test_create_namespaced_pod_eviction(self):
        """Test case for create_namespaced_pod_eviction

        """
        pass

    def test_create_namespaced_pod_template(self):
        """Test case for create_namespaced_pod_template

        """
        pass

    def test_create_namespaced_replication_controller(self):
        """Test case for create_namespaced_replication_controller

        """
        pass

    def test_create_namespaced_resource_quota(self):
        """Test case for create_namespaced_resource_quota

        """
        pass

    def test_create_namespaced_secret(self):
        """Test case for create_namespaced_secret

        """
        pass

    def test_create_namespaced_service(self):
        """Test case for create_namespaced_service

        """
        pass

    def test_create_namespaced_service_account(self):
        """Test case for create_namespaced_service_account

        """
        pass

    def test_create_namespaced_service_account_token(self):
        """Test case for create_namespaced_service_account_token

        """
        pass

    def test_create_node(self):
        """Test case for create_node

        """
        pass

    def test_create_persistent_volume(self):
        """Test case for create_persistent_volume

        """
        pass

    def test_delete_collection_namespaced_config_map(self):
        """Test case for delete_collection_namespaced_config_map

        """
        pass

    def test_delete_collection_namespaced_endpoints(self):
        """Test case for delete_collection_namespaced_endpoints

        """
        pass

    def test_delete_collection_namespaced_event(self):
        """Test case for delete_collection_namespaced_event

        """
        pass

    def test_delete_collection_namespaced_limit_range(self):
        """Test case for delete_collection_namespaced_limit_range

        """
        pass

    def test_delete_collection_namespaced_persistent_volume_claim(self):
        """Test case for delete_collection_namespaced_persistent_volume_claim

        """
        pass

    def test_delete_collection_namespaced_pod(self):
        """Test case for delete_collection_namespaced_pod

        """
        pass

    def test_delete_collection_namespaced_pod_template(self):
        """Test case for delete_collection_namespaced_pod_template

        """
        pass

    def test_delete_collection_namespaced_replication_controller(self):
        """Test case for delete_collection_namespaced_replication_controller

        """
        pass

    def test_delete_collection_namespaced_resource_quota(self):
        """Test case for delete_collection_namespaced_resource_quota

        """
        pass

    def test_delete_collection_namespaced_secret(self):
        """Test case for delete_collection_namespaced_secret

        """
        pass

    def test_delete_collection_namespaced_service_account(self):
        """Test case for delete_collection_namespaced_service_account

        """
        pass

    def test_delete_collection_node(self):
        """Test case for delete_collection_node

        """
        pass

    def test_delete_collection_persistent_volume(self):
        """Test case for delete_collection_persistent_volume

        """
        pass

    def test_delete_namespace(self):
        """Test case for delete_namespace

        """
        pass

    def test_delete_namespaced_config_map(self):
        """Test case for delete_namespaced_config_map

        """
        pass

    def test_delete_namespaced_endpoints(self):
        """Test case for delete_namespaced_endpoints

        """
        pass

    def test_delete_namespaced_event(self):
        """Test case for delete_namespaced_event

        """
        pass

    def test_delete_namespaced_limit_range(self):
        """Test case for delete_namespaced_limit_range

        """
        pass

    def test_delete_namespaced_persistent_volume_claim(self):
        """Test case for delete_namespaced_persistent_volume_claim

        """
        pass

    def test_delete_namespaced_pod(self):
        """Test case for delete_namespaced_pod

        """
        pass

    def test_delete_namespaced_pod_template(self):
        """Test case for delete_namespaced_pod_template

        """
        pass

    def test_delete_namespaced_replication_controller(self):
        """Test case for delete_namespaced_replication_controller

        """
        pass

    def test_delete_namespaced_resource_quota(self):
        """Test case for delete_namespaced_resource_quota

        """
        pass

    def test_delete_namespaced_secret(self):
        """Test case for delete_namespaced_secret

        """
        pass

    def test_delete_namespaced_service(self):
        """Test case for delete_namespaced_service

        """
        pass

    def test_delete_namespaced_service_account(self):
        """Test case for delete_namespaced_service_account

        """
        pass

    def test_delete_node(self):
        """Test case for delete_node

        """
        pass

    def test_delete_persistent_volume(self):
        """Test case for delete_persistent_volume

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_component_status(self):
        """Test case for list_component_status

        """
        pass

    def test_list_config_map_for_all_namespaces(self):
        """Test case for list_config_map_for_all_namespaces

        """
        pass

    def test_list_endpoints_for_all_namespaces(self):
        """Test case for list_endpoints_for_all_namespaces

        """
        pass

    def test_list_event_for_all_namespaces(self):
        """Test case for list_event_for_all_namespaces

        """
        pass

    def test_list_limit_range_for_all_namespaces(self):
        """Test case for list_limit_range_for_all_namespaces

        """
        pass

    def test_list_namespace(self):
        """Test case for list_namespace

        """
        pass

    def test_list_namespaced_config_map(self):
        """Test case for list_namespaced_config_map

        """
        pass

    def test_list_namespaced_endpoints(self):
        """Test case for list_namespaced_endpoints

        """
        pass

    def test_list_namespaced_event(self):
        """Test case for list_namespaced_event

        """
        pass

    def test_list_namespaced_limit_range(self):
        """Test case for list_namespaced_limit_range

        """
        pass

    def test_list_namespaced_persistent_volume_claim(self):
        """Test case for list_namespaced_persistent_volume_claim

        """
        pass

    def test_list_namespaced_pod(self):
        """Test case for list_namespaced_pod

        """
        pass

    def test_list_namespaced_pod_template(self):
        """Test case for list_namespaced_pod_template

        """
        pass

    def test_list_namespaced_replication_controller(self):
        """Test case for list_namespaced_replication_controller

        """
        pass

    def test_list_namespaced_resource_quota(self):
        """Test case for list_namespaced_resource_quota

        """
        pass

    def test_list_namespaced_secret(self):
        """Test case for list_namespaced_secret

        """
        pass

    def test_list_namespaced_service(self):
        """Test case for list_namespaced_service

        """
        pass

    def test_list_namespaced_service_account(self):
        """Test case for list_namespaced_service_account

        """
        pass

    def test_list_node(self):
        """Test case for list_node

        """
        pass

    def test_list_persistent_volume(self):
        """Test case for list_persistent_volume

        """
        pass

    def test_list_persistent_volume_claim_for_all_namespaces(self):
        """Test case for list_persistent_volume_claim_for_all_namespaces

        """
        pass

    def test_list_pod_for_all_namespaces(self):
        """Test case for list_pod_for_all_namespaces

        """
        pass

    def test_list_pod_template_for_all_namespaces(self):
        """Test case for list_pod_template_for_all_namespaces

        """
        pass

    def test_list_replication_controller_for_all_namespaces(self):
        """Test case for list_replication_controller_for_all_namespaces

        """
        pass

    def test_list_resource_quota_for_all_namespaces(self):
        """Test case for list_resource_quota_for_all_namespaces

        """
        pass

    def test_list_secret_for_all_namespaces(self):
        """Test case for list_secret_for_all_namespaces

        """
        pass

    def test_list_service_account_for_all_namespaces(self):
        """Test case for list_service_account_for_all_namespaces

        """
        pass

    def test_list_service_for_all_namespaces(self):
        """Test case for list_service_for_all_namespaces

        """
        pass

    def test_patch_namespace(self):
        """Test case for patch_namespace

        """
        pass

    def test_patch_namespace_status(self):
        """Test case for patch_namespace_status

        """
        pass

    def test_patch_namespaced_config_map(self):
        """Test case for patch_namespaced_config_map

        """
        pass

    def test_patch_namespaced_endpoints(self):
        """Test case for patch_namespaced_endpoints

        """
        pass

    def test_patch_namespaced_event(self):
        """Test case for patch_namespaced_event

        """
        pass

    def test_patch_namespaced_limit_range(self):
        """Test case for patch_namespaced_limit_range

        """
        pass

    def test_patch_namespaced_persistent_volume_claim(self):
        """Test case for patch_namespaced_persistent_volume_claim

        """
        pass

    def test_patch_namespaced_persistent_volume_claim_status(self):
        """Test case for patch_namespaced_persistent_volume_claim_status

        """
        pass

    def test_patch_namespaced_pod(self):
        """Test case for patch_namespaced_pod

        """
        pass

    def test_patch_namespaced_pod_status(self):
        """Test case for patch_namespaced_pod_status

        """
        pass

    def test_patch_namespaced_pod_template(self):
        """Test case for patch_namespaced_pod_template

        """
        pass

    def test_patch_namespaced_replication_controller(self):
        """Test case for patch_namespaced_replication_controller

        """
        pass

    def test_patch_namespaced_replication_controller_scale(self):
        """Test case for patch_namespaced_replication_controller_scale

        """
        pass

    def test_patch_namespaced_replication_controller_status(self):
        """Test case for patch_namespaced_replication_controller_status

        """
        pass

    def test_patch_namespaced_resource_quota(self):
        """Test case for patch_namespaced_resource_quota

        """
        pass

    def test_patch_namespaced_resource_quota_status(self):
        """Test case for patch_namespaced_resource_quota_status

        """
        pass

    def test_patch_namespaced_secret(self):
        """Test case for patch_namespaced_secret

        """
        pass

    def test_patch_namespaced_service(self):
        """Test case for patch_namespaced_service

        """
        pass

    def test_patch_namespaced_service_account(self):
        """Test case for patch_namespaced_service_account

        """
        pass

    def test_patch_namespaced_service_status(self):
        """Test case for patch_namespaced_service_status

        """
        pass

    def test_patch_node(self):
        """Test case for patch_node

        """
        pass

    def test_patch_node_status(self):
        """Test case for patch_node_status

        """
        pass

    def test_patch_persistent_volume(self):
        """Test case for patch_persistent_volume

        """
        pass

    def test_patch_persistent_volume_status(self):
        """Test case for patch_persistent_volume_status

        """
        pass

    def test_read_component_status(self):
        """Test case for read_component_status

        """
        pass

    def test_read_namespace(self):
        """Test case for read_namespace

        """
        pass

    def test_read_namespace_status(self):
        """Test case for read_namespace_status

        """
        pass

    def test_read_namespaced_config_map(self):
        """Test case for read_namespaced_config_map

        """
        pass

    def test_read_namespaced_endpoints(self):
        """Test case for read_namespaced_endpoints

        """
        pass

    def test_read_namespaced_event(self):
        """Test case for read_namespaced_event

        """
        pass

    def test_read_namespaced_limit_range(self):
        """Test case for read_namespaced_limit_range

        """
        pass

    def test_read_namespaced_persistent_volume_claim(self):
        """Test case for read_namespaced_persistent_volume_claim

        """
        pass

    def test_read_namespaced_persistent_volume_claim_status(self):
        """Test case for read_namespaced_persistent_volume_claim_status

        """
        pass

    def test_read_namespaced_pod(self):
        """Test case for read_namespaced_pod

        """
        pass

    def test_read_namespaced_pod_log(self):
        """Test case for read_namespaced_pod_log

        """
        pass

    def test_read_namespaced_pod_status(self):
        """Test case for read_namespaced_pod_status

        """
        pass

    def test_read_namespaced_pod_template(self):
        """Test case for read_namespaced_pod_template

        """
        pass

    def test_read_namespaced_replication_controller(self):
        """Test case for read_namespaced_replication_controller

        """
        pass

    def test_read_namespaced_replication_controller_scale(self):
        """Test case for read_namespaced_replication_controller_scale

        """
        pass

    def test_read_namespaced_replication_controller_status(self):
        """Test case for read_namespaced_replication_controller_status

        """
        pass

    def test_read_namespaced_resource_quota(self):
        """Test case for read_namespaced_resource_quota

        """
        pass

    def test_read_namespaced_resource_quota_status(self):
        """Test case for read_namespaced_resource_quota_status

        """
        pass

    def test_read_namespaced_secret(self):
        """Test case for read_namespaced_secret

        """
        pass

    def test_read_namespaced_service(self):
        """Test case for read_namespaced_service

        """
        pass

    def test_read_namespaced_service_account(self):
        """Test case for read_namespaced_service_account

        """
        pass

    def test_read_namespaced_service_status(self):
        """Test case for read_namespaced_service_status

        """
        pass

    def test_read_node(self):
        """Test case for read_node

        """
        pass

    def test_read_node_status(self):
        """Test case for read_node_status

        """
        pass

    def test_read_persistent_volume(self):
        """Test case for read_persistent_volume

        """
        pass

    def test_read_persistent_volume_status(self):
        """Test case for read_persistent_volume_status

        """
        pass

    def test_replace_namespace(self):
        """Test case for replace_namespace

        """
        pass

    def test_replace_namespace_finalize(self):
        """Test case for replace_namespace_finalize

        """
        pass

    def test_replace_namespace_status(self):
        """Test case for replace_namespace_status

        """
        pass

    def test_replace_namespaced_config_map(self):
        """Test case for replace_namespaced_config_map

        """
        pass

    def test_replace_namespaced_endpoints(self):
        """Test case for replace_namespaced_endpoints

        """
        pass

    def test_replace_namespaced_event(self):
        """Test case for replace_namespaced_event

        """
        pass

    def test_replace_namespaced_limit_range(self):
        """Test case for replace_namespaced_limit_range

        """
        pass

    def test_replace_namespaced_persistent_volume_claim(self):
        """Test case for replace_namespaced_persistent_volume_claim

        """
        pass

    def test_replace_namespaced_persistent_volume_claim_status(self):
        """Test case for replace_namespaced_persistent_volume_claim_status

        """
        pass

    def test_replace_namespaced_pod(self):
        """Test case for replace_namespaced_pod

        """
        pass

    def test_replace_namespaced_pod_status(self):
        """Test case for replace_namespaced_pod_status

        """
        pass

    def test_replace_namespaced_pod_template(self):
        """Test case for replace_namespaced_pod_template

        """
        pass

    def test_replace_namespaced_replication_controller(self):
        """Test case for replace_namespaced_replication_controller

        """
        pass

    def test_replace_namespaced_replication_controller_scale(self):
        """Test case for replace_namespaced_replication_controller_scale

        """
        pass

    def test_replace_namespaced_replication_controller_status(self):
        """Test case for replace_namespaced_replication_controller_status

        """
        pass

    def test_replace_namespaced_resource_quota(self):
        """Test case for replace_namespaced_resource_quota

        """
        pass

    def test_replace_namespaced_resource_quota_status(self):
        """Test case for replace_namespaced_resource_quota_status

        """
        pass

    def test_replace_namespaced_secret(self):
        """Test case for replace_namespaced_secret

        """
        pass

    def test_replace_namespaced_service(self):
        """Test case for replace_namespaced_service

        """
        pass

    def test_replace_namespaced_service_account(self):
        """Test case for replace_namespaced_service_account

        """
        pass

    def test_replace_namespaced_service_status(self):
        """Test case for replace_namespaced_service_status

        """
        pass

    def test_replace_node(self):
        """Test case for replace_node

        """
        pass

    def test_replace_node_status(self):
        """Test case for replace_node_status

        """
        pass

    def test_replace_persistent_volume(self):
        """Test case for replace_persistent_volume

        """
        pass

    def test_replace_persistent_volume_status(self):
        """Test case for replace_persistent_volume_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
