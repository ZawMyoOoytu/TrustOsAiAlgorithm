class BillingEngine:
    def check(self, user_id, task_type):
        return {"allowed": True}

    def deduct(self, user_id, task_type):
        return True