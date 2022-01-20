from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()

    if network.show_active() != "development":
        pride_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"the active network is {network.show_active()}")
        print("Deploying Mocks...")
        mock_agg = MockV3Aggregator.deploy(18, 200000000000000000, {"from": account})
        print("Mocks deployed")
        pride_feed_address = mock_agg.address

    fund_me = FundMe.deploy(
        pride_feed_address,
        {"from": account},
        publish_source=True,
    )

    # print("contract deployed to {fund_me.address}")
    # pass


def main():
    deploy_fund_me()
