# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LoginWhiteLabelingParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'admin_settings_id': 'str',
        'app_title': 'str',
        'dark_foreground': 'bool',
        'domain_name': 'str',
        'enable_help_links': 'bool',
        'favicon': 'Favicon',
        'favicon_checksum': 'str',
        'help_link_base_url': 'str',
        'logo_image_checksum': 'str',
        'logo_image_height': 'int',
        'logo_image_url': 'str',
        'page_background_color': 'str',
        'palette_settings': 'PaletteSettings',
        'platform_name': 'str',
        'platform_version': 'str',
        'show_name_bottom': 'bool',
        'show_name_version': 'bool',
        'white_labeling_enabled': 'bool'
    }

    attribute_map = {
        'admin_settings_id': 'adminSettingsId',
        'app_title': 'appTitle',
        'dark_foreground': 'darkForeground',
        'domain_name': 'domainName',
        'enable_help_links': 'enableHelpLinks',
        'favicon': 'favicon',
        'favicon_checksum': 'faviconChecksum',
        'help_link_base_url': 'helpLinkBaseUrl',
        'logo_image_checksum': 'logoImageChecksum',
        'logo_image_height': 'logoImageHeight',
        'logo_image_url': 'logoImageUrl',
        'page_background_color': 'pageBackgroundColor',
        'palette_settings': 'paletteSettings',
        'platform_name': 'platformName',
        'platform_version': 'platformVersion',
        'show_name_bottom': 'showNameBottom',
        'show_name_version': 'showNameVersion',
        'white_labeling_enabled': 'whiteLabelingEnabled'
    }

    def __init__(self, admin_settings_id=None, app_title=None, dark_foreground=None, domain_name=None, enable_help_links=None, favicon=None, favicon_checksum=None, help_link_base_url=None, logo_image_checksum=None, logo_image_height=None, logo_image_url=None, page_background_color=None, palette_settings=None, platform_name=None, platform_version=None, show_name_bottom=None, show_name_version=None, white_labeling_enabled=None):  # noqa: E501
        """LoginWhiteLabelingParams - a model defined in Swagger"""  # noqa: E501
        self._admin_settings_id = None
        self._app_title = None
        self._dark_foreground = None
        self._domain_name = None
        self._enable_help_links = None
        self._favicon = None
        self._favicon_checksum = None
        self._help_link_base_url = None
        self._logo_image_checksum = None
        self._logo_image_height = None
        self._logo_image_url = None
        self._page_background_color = None
        self._palette_settings = None
        self._platform_name = None
        self._platform_version = None
        self._show_name_bottom = None
        self._show_name_version = None
        self._white_labeling_enabled = None
        self.discriminator = None
        if admin_settings_id is not None:
            self.admin_settings_id = admin_settings_id
        if app_title is not None:
            self.app_title = app_title
        if dark_foreground is not None:
            self.dark_foreground = dark_foreground
        if domain_name is not None:
            self.domain_name = domain_name
        if enable_help_links is not None:
            self.enable_help_links = enable_help_links
        if favicon is not None:
            self.favicon = favicon
        if favicon_checksum is not None:
            self.favicon_checksum = favicon_checksum
        if help_link_base_url is not None:
            self.help_link_base_url = help_link_base_url
        if logo_image_checksum is not None:
            self.logo_image_checksum = logo_image_checksum
        if logo_image_height is not None:
            self.logo_image_height = logo_image_height
        if logo_image_url is not None:
            self.logo_image_url = logo_image_url
        if page_background_color is not None:
            self.page_background_color = page_background_color
        if palette_settings is not None:
            self.palette_settings = palette_settings
        if platform_name is not None:
            self.platform_name = platform_name
        if platform_version is not None:
            self.platform_version = platform_version
        if show_name_bottom is not None:
            self.show_name_bottom = show_name_bottom
        if show_name_version is not None:
            self.show_name_version = show_name_version
        if white_labeling_enabled is not None:
            self.white_labeling_enabled = white_labeling_enabled

    @property
    def admin_settings_id(self):
        """Gets the admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._admin_settings_id

    @admin_settings_id.setter
    def admin_settings_id(self, admin_settings_id):
        """Sets the admin_settings_id of this LoginWhiteLabelingParams.


        :param admin_settings_id: The admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._admin_settings_id = admin_settings_id

    @property
    def app_title(self):
        """Gets the app_title of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The app_title of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._app_title

    @app_title.setter
    def app_title(self, app_title):
        """Sets the app_title of this LoginWhiteLabelingParams.


        :param app_title: The app_title of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._app_title = app_title

    @property
    def dark_foreground(self):
        """Gets the dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._dark_foreground

    @dark_foreground.setter
    def dark_foreground(self, dark_foreground):
        """Sets the dark_foreground of this LoginWhiteLabelingParams.


        :param dark_foreground: The dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._dark_foreground = dark_foreground

    @property
    def domain_name(self):
        """Gets the domain_name of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The domain_name of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this LoginWhiteLabelingParams.


        :param domain_name: The domain_name of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def enable_help_links(self):
        """Gets the enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_help_links

    @enable_help_links.setter
    def enable_help_links(self, enable_help_links):
        """Sets the enable_help_links of this LoginWhiteLabelingParams.


        :param enable_help_links: The enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._enable_help_links = enable_help_links

    @property
    def favicon(self):
        """Gets the favicon of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The favicon of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: Favicon
        """
        return self._favicon

    @favicon.setter
    def favicon(self, favicon):
        """Sets the favicon of this LoginWhiteLabelingParams.


        :param favicon: The favicon of this LoginWhiteLabelingParams.  # noqa: E501
        :type: Favicon
        """

        self._favicon = favicon

    @property
    def favicon_checksum(self):
        """Gets the favicon_checksum of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The favicon_checksum of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._favicon_checksum

    @favicon_checksum.setter
    def favicon_checksum(self, favicon_checksum):
        """Sets the favicon_checksum of this LoginWhiteLabelingParams.


        :param favicon_checksum: The favicon_checksum of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._favicon_checksum = favicon_checksum

    @property
    def help_link_base_url(self):
        """Gets the help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._help_link_base_url

    @help_link_base_url.setter
    def help_link_base_url(self, help_link_base_url):
        """Sets the help_link_base_url of this LoginWhiteLabelingParams.


        :param help_link_base_url: The help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._help_link_base_url = help_link_base_url

    @property
    def logo_image_checksum(self):
        """Gets the logo_image_checksum of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The logo_image_checksum of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._logo_image_checksum

    @logo_image_checksum.setter
    def logo_image_checksum(self, logo_image_checksum):
        """Sets the logo_image_checksum of this LoginWhiteLabelingParams.


        :param logo_image_checksum: The logo_image_checksum of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._logo_image_checksum = logo_image_checksum

    @property
    def logo_image_height(self):
        """Gets the logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: int
        """
        return self._logo_image_height

    @logo_image_height.setter
    def logo_image_height(self, logo_image_height):
        """Sets the logo_image_height of this LoginWhiteLabelingParams.


        :param logo_image_height: The logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501
        :type: int
        """

        self._logo_image_height = logo_image_height

    @property
    def logo_image_url(self):
        """Gets the logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._logo_image_url

    @logo_image_url.setter
    def logo_image_url(self, logo_image_url):
        """Sets the logo_image_url of this LoginWhiteLabelingParams.


        :param logo_image_url: The logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._logo_image_url = logo_image_url

    @property
    def page_background_color(self):
        """Gets the page_background_color of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The page_background_color of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._page_background_color

    @page_background_color.setter
    def page_background_color(self, page_background_color):
        """Sets the page_background_color of this LoginWhiteLabelingParams.


        :param page_background_color: The page_background_color of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._page_background_color = page_background_color

    @property
    def palette_settings(self):
        """Gets the palette_settings of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The palette_settings of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: PaletteSettings
        """
        return self._palette_settings

    @palette_settings.setter
    def palette_settings(self, palette_settings):
        """Sets the palette_settings of this LoginWhiteLabelingParams.


        :param palette_settings: The palette_settings of this LoginWhiteLabelingParams.  # noqa: E501
        :type: PaletteSettings
        """

        self._palette_settings = palette_settings

    @property
    def platform_name(self):
        """Gets the platform_name of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The platform_name of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this LoginWhiteLabelingParams.


        :param platform_name: The platform_name of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def platform_version(self):
        """Gets the platform_version of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The platform_version of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """Sets the platform_version of this LoginWhiteLabelingParams.


        :param platform_version: The platform_version of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._platform_version = platform_version

    @property
    def show_name_bottom(self):
        """Gets the show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_name_bottom

    @show_name_bottom.setter
    def show_name_bottom(self, show_name_bottom):
        """Sets the show_name_bottom of this LoginWhiteLabelingParams.


        :param show_name_bottom: The show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._show_name_bottom = show_name_bottom

    @property
    def show_name_version(self):
        """Gets the show_name_version of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The show_name_version of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_name_version

    @show_name_version.setter
    def show_name_version(self, show_name_version):
        """Sets the show_name_version of this LoginWhiteLabelingParams.


        :param show_name_version: The show_name_version of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._show_name_version = show_name_version

    @property
    def white_labeling_enabled(self):
        """Gets the white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._white_labeling_enabled

    @white_labeling_enabled.setter
    def white_labeling_enabled(self, white_labeling_enabled):
        """Sets the white_labeling_enabled of this LoginWhiteLabelingParams.


        :param white_labeling_enabled: The white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._white_labeling_enabled = white_labeling_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LoginWhiteLabelingParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginWhiteLabelingParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other