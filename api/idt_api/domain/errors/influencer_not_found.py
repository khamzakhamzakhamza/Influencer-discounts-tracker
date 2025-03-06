class InfluencerNotFound(Exception):
    def __init__(self, link):
        message = f"Influencer not found: {link}"
        super().__init__(message)
        self.code = 1000
