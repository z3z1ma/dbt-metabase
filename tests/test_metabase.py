import unittest

from dbtmetabase.metabase import MetabaseClient
from dbtmetabase.models.metabase import (
    MetabaseModel,
    MetabaseColumn,
)

import logging
import json
import yaml
import os


MODELS = [
    MetabaseModel(
        name="ORDERS",
        schema="PUBLIC",
        description="This table has basic information about orders, as well as some derived facts based on payments",
        model_key="nodes",
        ref="ref('orders')",
        columns=[
            MetabaseColumn(
                name="ORDER_ID",
                description="This is a unique identifier for an order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="CUSTOMER_ID",
                description="Foreign key to the customers table",
                meta_fields={},
                semantic_type="type/FK",
                visibility_type=None,
                fk_target_table="PUBLIC.CUSTOMERS",
                fk_target_field="CUSTOMER_ID",
            ),
            MetabaseColumn(
                name="ORDER_DATE",
                description="Date (UTC) that the order was placed",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="STATUS",
                description="Orders can be one of the following statuses:\n\n| status         | description                                                                                                            |\n|----------------|------------------------------------------------------------------------------------------------------------------------|\n| placed         | The order has been placed but has not yet left the warehouse                                                           |\n| shipped        | The order has ben shipped to the customer and is currently in transit                                                  |\n| completed      | The order has been received by the customer                                                                            |\n| return_pending | The customer has indicated that they would like to return the order, but it has not yet been received at the warehouse |\n| returned       | The order has been returned by the customer and received at the warehouse                                              |",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="AMOUNT",
                description="Total amount (AUD) of the order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="CREDIT_CARD_AMOUNT",
                description="Amount of the order (AUD) paid for by credit card",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="COUPON_AMOUNT",
                description="Amount of the order (AUD) paid for by coupon",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="BANK_TRANSFER_AMOUNT",
                description="Amount of the order (AUD) paid for by bank transfer",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="GIFT_CARD_AMOUNT",
                description="Amount of the order (AUD) paid for by gift card",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    MetabaseModel(
        name="CUSTOMERS",
        schema="PUBLIC",
        description="This table has basic information about a customer, as well as some derived facts based on a customer's orders",
        model_key="nodes",
        ref="ref('customers')",
        columns=[
            MetabaseColumn(
                name="CUSTOMER_ID",
                description="This is a unique identifier for a customer",
                meta_fields={},
                semantic_type="type/FK",
                visibility_type=None,
                fk_target_table="PUBLIC.ORDERS",
                fk_target_field="CUSTOMER_ID",
            ),
            MetabaseColumn(
                name="FIRST_NAME",
                description="Customer's first name. PII.",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="LAST_NAME",
                description="Customer's last name. PII.",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="FIRST_ORDER",
                description="Date (UTC) of a customer's first order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="MOST_RECENT_ORDER",
                description="Date (UTC) of a customer's most recent order",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="NUMBER_OF_ORDERS",
                description="Count of the number of orders a customer has placed",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="TOTAL_ORDER_AMOUNT",
                description="Total value (AUD) of a customer's orders",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    MetabaseModel(
        name="STG_ORDERS",
        schema="PUBLIC",
        description="",
        model_key="nodes",
        ref="ref('stg_orders')",
        columns=[
            MetabaseColumn(
                name="ORDER_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="STATUS",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    MetabaseModel(
        name="STG_PAYMENTS",
        schema="PUBLIC",
        description="",
        model_key="nodes",
        ref="ref('stg_payments')",
        columns=[
            MetabaseColumn(
                name="PAYMENT_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
            MetabaseColumn(
                name="PAYMENT_METHOD",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            ),
        ],
    ),
    MetabaseModel(
        name="STG_CUSTOMERS",
        schema="PUBLIC",
        description="",
        model_key="nodes",
        ref="ref('stg_customers')",
        columns=[
            MetabaseColumn(
                name="CUSTOMER_ID",
                description="",
                meta_fields={},
                semantic_type=None,
                visibility_type=None,
                fk_target_table=None,
                fk_target_field=None,
            )
        ],
    ),
]


class MockMetabaseClient(MetabaseClient):
    def get_session_id(self, user: str, password: str) -> str:
        return "dummy"

    def api(self, method: str, path: str):
        BASE_PATH = "tests/fixtures/mock_api/"
        if method == "get":
            if os.path.exists(f"{BASE_PATH}/{path.lstrip('/')}.json"):
                return json.load(open(f"{BASE_PATH}/{path.lstrip('/')}.json"))
            else:
                return {}


class TestMetabaseClient(unittest.TestCase):
    def setUp(self):
        self.client = MockMetabaseClient(
            host="localhost:3000",
            user="dummy",
            password="dummy",
            use_http=True,
        )
        logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def test_exposures(self):
        mbc = self.client
        mbc.extract_exposures(
            MODELS,
            output_name="unittest_exposures",
            output_path="tests/fixtures/exposure/",
        )
        # Baseline in SCM
        baseline = yaml.safe_load(
            open("tests/fixtures/exposure/baseline_test_exposures.yml", "r")
        )
        # Load from YAML and tear down
        sample = yaml.safe_load(
            open("tests/fixtures/exposure/unittest_exposures.yml", "r")
        )

        baseline_exposures = sorted(baseline["exposures"], key=lambda ele: ele["name"])
        sample_exposures = sorted(sample["exposures"], key=lambda ele: ele["name"])

        self.assertEqual(baseline_exposures, sample_exposures)
