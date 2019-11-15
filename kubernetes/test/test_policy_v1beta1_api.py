# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: v1.15.7
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.policy_v1beta1_api import PolicyV1beta1Api  # noqa: E501
from kubernetes.client.rest import ApiException


class TestPolicyV1beta1Api(unittest.TestCase):
    """PolicyV1beta1Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.policy_v1beta1_api.PolicyV1beta1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_pod_disruption_budget(self):
        """Test case for create_namespaced_pod_disruption_budget

        """
        pass

    def test_create_pod_security_policy(self):
        """Test case for create_pod_security_policy

        """
        pass

    def test_delete_collection_namespaced_pod_disruption_budget(self):
        """Test case for delete_collection_namespaced_pod_disruption_budget

        """
        pass

    def test_delete_collection_pod_security_policy(self):
        """Test case for delete_collection_pod_security_policy

        """
        pass

    def test_delete_namespaced_pod_disruption_budget(self):
        """Test case for delete_namespaced_pod_disruption_budget

        """
        pass

    def test_delete_pod_security_policy(self):
        """Test case for delete_pod_security_policy

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_namespaced_pod_disruption_budget(self):
        """Test case for list_namespaced_pod_disruption_budget

        """
        pass

    def test_list_pod_disruption_budget_for_all_namespaces(self):
        """Test case for list_pod_disruption_budget_for_all_namespaces

        """
        pass

    def test_list_pod_security_policy(self):
        """Test case for list_pod_security_policy

        """
        pass

    def test_patch_namespaced_pod_disruption_budget(self):
        """Test case for patch_namespaced_pod_disruption_budget

        """
        pass

    def test_patch_namespaced_pod_disruption_budget_status(self):
        """Test case for patch_namespaced_pod_disruption_budget_status

        """
        pass

    def test_patch_pod_security_policy(self):
        """Test case for patch_pod_security_policy

        """
        pass

    def test_read_namespaced_pod_disruption_budget(self):
        """Test case for read_namespaced_pod_disruption_budget

        """
        pass

    def test_read_namespaced_pod_disruption_budget_status(self):
        """Test case for read_namespaced_pod_disruption_budget_status

        """
        pass

    def test_read_pod_security_policy(self):
        """Test case for read_pod_security_policy

        """
        pass

    def test_replace_namespaced_pod_disruption_budget(self):
        """Test case for replace_namespaced_pod_disruption_budget

        """
        pass

    def test_replace_namespaced_pod_disruption_budget_status(self):
        """Test case for replace_namespaced_pod_disruption_budget_status

        """
        pass

    def test_replace_pod_security_policy(self):
        """Test case for replace_pod_security_policy

        """
        pass


if __name__ == '__main__':
    unittest.main()
