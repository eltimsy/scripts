city_views = self.ga_request(
            metrics='ga:pageviews',
            filters='ga:city==Toronto,ga:eventAction==family-gp',
            max_results=10,
        )
