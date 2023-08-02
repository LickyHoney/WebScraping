import configparser
import json
import logging



class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level


class Config:
    def __init__(self, config_file):
        self._config = configparser.RawConfigParser(comment_prefixes='#')
        self._config.read(config_file, encoding='utf8')

        # General
        with open(self._config['General']['keywords_file'], encoding='utf-8') as f:
            string1 = self.keywords = json.load(f)
            print(string1)
        # with open(self._config['General']['trend_keywords_file'], encoding='utf-8') as f:   
        #     string2 = self.trend_keywords = json.load(f)
        #     print(string2)
        # with open(self._config['General']['blacklist_file'], 'r', encoding='utf-8') as f:
        #     string3 = self.blacklist = json.load(f)
        #     print(string3)
        # self.save_dir = self._config['General']['save_dir']
        # self.ending_soon_days = int(self._config['General']['ending_soon_days'])
        # self.posted_recently_days = int(self._config['General']['posted_recently_days'])
        # self.errors_dir = self._config['General']['errors_dir']
        # self.max_line_len_for_regex = int(self._config['General']['max_line_len_for_regex'])
        # self.db_file = self._config['General']['db_file']
        # self.site_limit = self._config['General']['site_limit']
        self.logger = None
        #self.debug_log_file = self._config['General']['debug_log_file']
        # if len(self.debug_log_file) > 0:
        #     self.logger = logging.getLogger('debug')
        #     self.logger.setLevel(logging.DEBUG)
        #     handler = logging.FileHandler(self.debug_log_file)
        #     formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #     handler.setFormatter(formatter)
        #     # set filter to log only DEBUG lines
        #     handler.addFilter(MyFilter(logging.DEBUG))
        #     self.logger.addHandler(handler)
        # self.filter_title_with_keyword = self._config['General']['filter_title_with_keyword']
        # self.default_url_fetch_delay = int(self._config['General']['default_url_fetch_delay'])

        # Scheduling
        self.time = self._config['Scheduling']['time']
        self.interval = self._config['Scheduling']['interval']
        if self.interval:
            interval = [int(s) for s in self.interval.split(':')]
            self.interval = 60**2 * interval[0] + 60 * interval[1] + interval[2]
        self.run_pending_interval = int(self._config['Scheduling']['run_pending_interval'])

        # Email
        # self.smtp_server = self._config['Email']['smtp_server']
        # self.tls_smtp_port = int(self._config['Email']['tls_smtp_port'])
        # self.sender_user = self._config['Email']['sender_user']
        # self.sender_pwd = self._config['Email']['sender_pwd']
        # self.receivers = self._config['Email']['receivers'].split(',')

        # Jobly
        self.jobly = self._Website('Jobly', self._config)

        # LinkedIn
        self.linkedin = self._Website('LinkedIn', self._config)

        # Oikotie
        self.oikotie = self._Website('Oikotie', self._config)

        # Rekrytointi
        self.rekrytointi = self._Website('Rekrytointi', self._config)

        # Duunitori
        self.duunitori = self._Website('Duunitori', self._config)

    class _Website:
        def __init__(self, website, config):
            self.search_url = config[website]['search_url']
            self.title_link_regex = config[website]['title_link_regex']
            self.company_regex = config[website]['company_regex']
            self.location_regex = config[website]['location_regex']
            self.date_regex = config[website]['date_regex']
            self.end_date_regex = config[website]['end_date_regex']
            self.desc_regex = config[website]['desc_regex']

            if website in ('Jobly', 'Duunitori'):
                self.max_pages = int(config[website]['max_pages'])

            if website in ('LinkedIn',):
                self.url_fetch_delay = int(config[website]['url_fetch_delay'])

            if website == 'Duunitori':
                self.progress_regex = config[website]['progress_regex']

            if website == 'Oikotie':
                self.load_more_timeout = int(config[website]['load_more_timeout'])

                self.info_line_regex = config[website]['info_line_regex']

                self.title_link_regex2 = config[website]['title_link_regex2']
                self.cookies_iframe_id = config[website]['cookies_iframe_id']
                self.cookies_accept_xpath = config[website]['cookies_accept_xpath']
                self.load_button_xpath = config[website]['load_button_xpath']

            if website == 'Rekrytointi':
                self.load_more_timeout = int(config[website]['load_more_timeout'])

                self.info_line_regex = config[website]['info_line_regex']

                self.title_link_regex2 = config[website]['title_link_regex2']
                self.cookies_iframe_id = config[website]['cookies_iframe_id']
                self.cookies_accept_xpath = config[website]['cookies_accept_xpath']
                self.load_button_xpath = config[website]['load_button_xpath']


cfg = Config('./config.ini')
