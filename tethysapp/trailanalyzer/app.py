from tethys_sdk.base import TethysAppBase, url_map_maker


class MicroanalysisOfTrailElevationChanges(TethysAppBase):
    """
    Tethys app class for MicroAnalysis of Trail Elevation Changes.
    """

    name = 'Utah Trail Analyzer'
    index = 'trailanalyzer:home'
    icon = 'trailanalyzer/images/index.jpeg'
    model = 'trailanalyzer/images/model.jpg'
    options = 'trailanalyzer/images/options.jpg'
    package = 'trailanalyzer'
    root_url = 'trailanalyzer'
    color = '#0099ff'
    description = 'HIKING IS FUN!!!'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='trailanalyzer',
                           controller='trailanalyzer.controllers.home'),
                    UrlMap(name='map',
                           url='map',
                           controller='trailanalyzer.controllers.map'),
                    UrlMap(name='Video',
                           url='Video',
                           controller='trailanalyzer.controllers.Video'),
                    UrlMap(name='Help',
                           url='Help',
                           controller='trailanalyzer.controllers.Help'),
                    UrlMap(name='techdoc',
                           url='techdoc',
                           controller='trailanalyzer.controllers.techdoc'),

        )

        return url_maps