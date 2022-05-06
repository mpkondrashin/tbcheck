import requests
import xml.etree.cElementTree as ET


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

    def get_filters(self, profile_name, name, value):
        headers = {'X-SMS-API-KEY': self.api_key}
        url = f"https://{self.url}/ipsProfileMgmt/getFilters"
        xml = get_filters_request(profile_name, name, value)
        files = {'file': ('getFilters.xml', xml)}
        result = requests.post(url, files=files, headers=headers, verify=self.insecure_skip_verify)
        return result.text




        """
        s = Session()

        req = Request('POST', url, data=data, headers=headers)
        prepped = req.prepare()

        # do something with prepped.body
        prepped.body = 'No, I want exactly this as the body.'

        # do something with prepped.headers
        del prepped.headers['Content-Type']

        resp = s.send(prepped,
                      stream=stream,
                      verify=verify,
                      proxies=proxies,
                      cert=cert,
                      timeout=timeout
                      )

        print(resp.status_code)
        """


def get_filters_request(profile_name, name, value):
    if name not in ("number", "signature-id", "policy-id","name"):
        raise RuntimeError("Unsupported filter criteria: " + name)
    get_filters_element = ET.Element("getFilters")
    ET.SubElement(get_filters_element, "profile", attrib=dict(name=profile_name))
    filter_element = ET.SubElement(get_filters_element, "filter")
    ET.SubElement(filter_element, name).text = str(value)
    return ET.tostring(get_filters_element)


"""
p = result.prepare()
print(p)
print(p.body)
print(p.body.decode('ascii'))
print(result.)

"""