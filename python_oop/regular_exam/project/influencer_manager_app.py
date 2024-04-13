from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_TYPES = {'PremiumInfluencer': PremiumInfluencer, 'StandardInfluencer': StandardInfluencer}
    CAMAPIGN_TYPES = {'HighBudgetCampaign': HighBudgetCampaign, 'LowBudgetCampaign': LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        influencers_names = [i.username for i in self.influencers]
        if username in influencers_names:
            return f"{username} is already registered."

        new_influencer = self.INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.CAMAPIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        campaigns_ids = [c.campaign_id for c in self.campaigns]
        if campaign_id in campaigns_ids:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.CAMAPIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._get_influencer(influencer_username)
        campaign = self._get_campaign(campaign_id)

        if influencer is None:
            return f"Influencer '{influencer_username}' not found."

        if campaign is None:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet "
                    f"the eligibility criteria for the campaign with ID {campaign_id}.")

        payment = influencer.calculate_payment(campaign)
        if payment > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return (f"Influencer '{influencer_username}'"
                    f" has successfully participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        result = {}
        for campaign in self.campaigns:
            result[campaign] = 0
            for influencer in campaign.approved_influencers:
                result[campaign] += round(influencer.reached_followers(campaign.__class__.__name__))

        return result

    def influencer_campaign_report(self, username: str):
        influencer = self._get_influencer(username)
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget))
        result = "$$ Campaign Statistics $$\n"
        total_reached_followers_dict = self.calculate_total_reached_followers()
        for campaign in sorted_campaigns:
            result += (f"  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)},"
                       f" Total budget: ${campaign.budget:.2f}, "
                       f"Total reached followers: {total_reached_followers_dict[campaign]}\n")

        return result.strip()

    def _get_influencer(self, username):
        influencer = [i for i in self.influencers if i.username == username]
        return influencer[0] if influencer else None

    def _get_campaign(self, campaign_id):
        campaign = [c for c in self.campaigns if c.campaign_id == campaign_id]
        return campaign[0] if campaign else None

