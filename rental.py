import requests
from datetime import datetime, timedelta, date

class Rental:
    def __init__(self, url="http://localhost:5000", selected_rental=None):
        self.url = url
        self.selected_rental = selected_rental

    def create_rental(self, customer_id, video_id):
        query_params = {
            "customer_id": customer_id,
            "video_id": video_id
        }

        response = requests.post(self.url+"/rentals/check-out", json=query_params)
        return response.json()

    def list_rentals(self):
        response = requests.get(self.url+"/rentals")
        return response.json()

    def update_video(self, customer_id, video_id):
        for rental in self.list_rentals():
            if customer_id == rental["customer_id"] and video_id == rental["video_id"]:
                self.selected_rental = rental

        if self.selected_rental == None:
            return "Count not find rental by the customer id and video id"

        query_params = {
            "customer_id": customer_id,
            "video_id": video_id,
        }
        
        response = requests.post(self.url+"/rentals/check-in", json=query_params)
        return response.json()

    # def get_rentals_by_customer(self, customer_id=None):
    #     for rental in self.list_rentals():
    #         if rental["customer_id"] == customer_id:
    #             self.selected_rental = rental
        
    #     if self.selected_rental == None:
    #         return "Could not find rentals by that customer id"

    #     response = requests.get(self.url+f"/customers/{self.selected_rental['customer_id']}/rentals")
    #     return response.json()

    # def get_rentals_by_video(self, video_id=None):
    #     for rental in self.list_rentals():
    #         if rental["video_id"] == video_id:
    #             self.selected_rental = rental

    #     if self.selected_rental == None:
    #         return "Count not find rentals by that video id"

    #     response = requests.get(self.url+f"/videos/{self.selected_rental['video_id']}/rentals")
    #     return response.json()


