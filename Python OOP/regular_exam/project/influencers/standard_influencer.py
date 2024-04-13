from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.payment_percentage = 0.45

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * self.payment_percentage

        return payment

    def reached_followers(self, campaign_type: str):
        followers_multiplier_mapper = {'HighBudgetCampaign': 1.2, 'LowBudgetCampaign': 0.9}
        new_followers = self.followers * self.engagement_rate * followers_multiplier_mapper[campaign_type]


        return new_followers