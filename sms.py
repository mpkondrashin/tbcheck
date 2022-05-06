import requests
import urllib3
import xml.etree.cElementTree as ET

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

defaultUserAgent = 'TBCheck/0.1'


class SMS:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.user_agent = defaultUserAgent
        self.insecure_skip_verify = True

    def set_user_agent(self, user_agent):
        self.user_agent = user_agent
        return self

    def set_insecure_skip_verify(self, insecure_skip_verify):
        self.insecure_skip_verify = insecure_skip_verify
        return self

    def get_filter(self, profile_name, name, value):
        headers = {'X-SMS-API-KEY': self.api_key}
        url = f"https://{self.url}/ipsProfileMgmt/getFilters"
        xml = get_filters_request(profile_name, name, value)
        files = {'file': ('getFilters.xml', xml)}
        result = requests.post(url, files=files, headers=headers, verify=not self.insecure_skip_verify)
        #print(result.text)
        return ET.fromstring(result.text)

    def set_filter(self, xml_body):
        headers = {'X-SMS-API-KEY': self.api_key}
        url = f"https://{self.url}/ipsProfileMgmt/setFilters"
        files = {'file': ('setFilters.xml', xml_body)}
        result = requests.post(url, files=files, headers=headers, verify=not self.insecure_skip_verify)
        #print(result.text)
        #return ET.fromstring(result.text)
        return result.text

    def set_filters_action_set(self, profile_name, filter_number, refid):
        xml = set_filters_request(profile_name, filter_number, refid)
        # print("SET FILTERS_REQUEST XML", xml)
        return self.set_filter(xml)

    def action_set_refid(self, action_set_name):
        headers = {'X-SMS-API-KEY': self.api_key}
        url = f"https://{self.url}/dbAccess/tptDBServlet?method=DataDictionary&table=ACTIONSET&format=xml"
        result = requests.get(url, headers=headers, verify=not self.insecure_skip_verify)
        #print(result.text)
        root = ET.fromstring(result.text)
        action_sets = root.find('table/data')
        for row in action_sets.findall('r'):
            if row[1].text == action_set_name:
                return row[0].text
        return None


def get_filters_request(profile_name, name, value):
    if name not in ("number", "signature-id", "policy-id", "name"):
        raise RuntimeError("Unsupported filter criteria: " + name)
    get_filters_element = ET.Element("getFilters")
    ET.SubElement(get_filters_element, "profile", attrib=dict(name=profile_name))
    filter_element = ET.SubElement(get_filters_element, "filter")
    ET.SubElement(filter_element, name).text = str(value)
    xml = ET.tostring(get_filters_element)
    return xml

def set_filters_request(profile_name, filter_number, action_set_refid):
    get_filters_element = ET.Element('setFilters')
    ET.SubElement(get_filters_element, 'profile', attrib=dict(name=profile_name))
    filter_element = ET.SubElement(get_filters_element, 'filter')
    ET.SubElement(filter_element, 'number').text = str(filter_number)
    #ET.SubElement(filter_element, 'actionset', {'name': action_set})
    ET.SubElement(filter_element, 'actionset', {'refid': action_set_refid})
    xml = ET.tostring(get_filters_element)
    return xml

"""
p = result.prepare()
print(p)
print(p.body)
print(p.body.decode('ascii'))
print(result.)

"""