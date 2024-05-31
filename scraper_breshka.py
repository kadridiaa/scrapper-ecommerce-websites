import requests
import json
import sys

# Define headers
headers_ = {
    'Accept-Language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Origin': 'https://www.bershka.com',
    'Referer': 'https://www.bershka.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'accept': 'application/json',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}



if len(sys.argv) < 4:
    print("Usage: python scraper_bershka.py <query> <sexe> <hitsPerPage>")
    sys.exit(1)

# Get command-line arguments
query = sys.argv[1]
print(query)
sexe = sys.argv[2]
print(sexe)
hitsPerPage = sys.argv[3]

# Construct the data payload
if sexe and hitsPerPage:
    data = {
       "params":f"query={query}&analytics=true&analyticsTags=%5B%22dweb%22%2C%22country_dz%22%2C%22lang_fr%22%2C%22{sexe}%22%2C%22no_teen%22%2C%22season%22%2C%22store%22%5D&clickAnalytics=true&hitsPerPage={hitsPerPage}&ruleContexts=%5B%22dweb%22%2C%22country_dz%22%2C%22lang_fr%22%2C%22{sexe}%22%2C%22{sexe}_fr%22%5D&attributesToRetrieve=%5B%22pElement%22%5D&facets=%5B%22mainCategory%22%2C%22categoryNameEn%22%2C%22sizes%22%2C%22price%22%2C%22discount%22%2C%22colorNameFr%22%5D&facetFilters=%5B%5D&filters=&page=0"
    }
    print('first : ',data)
else:
    data = {
        "params": f"query={query}&analytics=true&analyticsTags=%5B%22dweb%22%2C%22country_dz%22%2C%22lang_fr%22%5D&clickAnalytics=true&hitsPerPage=10&ruleContexts=%5B%22dweb%22%2C%22country_dz%22%2C%22lang_fr%22%5D&attributesToRetrieve=%5B%22pElement%22%5D&facets=%5B%22mainCategory%22%2C%22categoryNameEn%22%2C%22sizes%22%2C%22price%22%2C%22discount%22%2C%22colorNameFr%22%5D&facetFilters=%5B%5D&filters=&page=0"
    }
    print('second',data)

data_json = json.dumps(data)
# print(data_json)


# Send the POST request
response = requests.post(
    'https://2kv2lbqg6e-dsn.algolia.net/1/indexes/pro_SEARCH_DZ/query?x-algolia-agent=Algolia%20for%20JavaScript%20(3.35.1)%3B%20Browser&x-algolia-application-id=2KV2LBQG6E&x-algolia-api-key=MGY4YzYzZWI2ZmRlYmYwOTM1ZGU2NGI3MjVjZjViMjgyMDIyYWM3NWEzZTM5ZjZiOWYwMzAyYThmNTkxMDUwMGF0dHJpYnV0ZXNUb0hpZ2hsaWdodD0lNUIlNUQmYXR0cmlidXRlc1RvU25pcHBldD0lNUIlNUQmZW5hYmxlUGVyc29uYWxpemF0aW9uPWZhbHNlJmVuYWJsZVJ1bGVzPXRydWUmZmFjZXRpbmdBZnRlckRpc3RpbmN0PXRydWUmZ2V0UmFua2luZ0luZm89dHJ1ZSZzbmlwcGV0RWxsaXBzaXNUZXh0PSVFMiU4MCVBNiZzdW1PckZpbHRlcnNTY29yZXM9dHJ1ZQ%3D%3D',
    headers=headers_,
    data=data_json,
)

# print(response.status_code)


# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    
    hits = response_data.get('hits', [])
    p_element_list = []
    
    # Append pElement for each hit to the list
    for hit in hits:
        pElement = hit.get('pElement')
        if pElement:
            p_element_list.append(str(pElement))
    
    # Join the pElement values into a single comma-separated string
    product_ids = ','.join(p_element_list)
    
    print(f"'productIds': '{product_ids}'")
else:
    print(f"Request failed with status code {response.status_code}")
    
# print(id_data)





cookies = {
    'FPID': 'FPID2.2.IaeNNYUwGhFnJMwISW2QP1VnWSDFarz1fjaPGLbn1Fg%3D.1709215063',
    'optimizelyEndUserId': 'oeu1709215070141r0.23047570243215176',
    '_gtmeec': 'e30%3D',
    '_fbp': 'fb.1.1709215073593.1194989933',
    'FPC': 'id=e5950294-3cce-4fba-abd8-bccac08d4e49',
    'BershkaGenderCategoryKey': 'BERSHKA_MAN',
    '_dyjsession': 'xzx6j0o9rf4ekxju0txoau0qvwqstfc6',
    'dy_fs_page': 'www.bershka.com%2Ffr%2Fh-man.html',
    '_dy_csc_ses': 'xzx6j0o9rf4ekxju0txoau0qvwqstfc6',
    '_dy_c_exps': '',
    '_dy_c_att_exps': '',
    '_gid': 'GA1.2.861255091.1716042332',
    '_dycnst': 'dg',
    '_dyid': '-3404720367395107493',
    '_dy_geo': 'DZ.AF.DZ_34.DZ_34_',
    '_dy_df_geo': 'Algeria..',
    'FPLC': 'z80KxOPh1zi2mPCJN2hu9emK7i8Zxioe0dfavBDd1lBUVCGclXP1OQ04pHSAIjQZlZHzC5f94DXPppoAwpJpzUIqdt6CvaQi8f3SJOVSBKFoYOS1SEsHWihkbQk9bQ%3D%3D',
    '_scid': '64d92825-a826-401e-81bd-d2a80c1aed32',
    '_tt_enable_cookie': '1',
    '_ttp': 'UbQeyBRVBQiWwgG_mdgdEgI5m2t',
    '_sctr': '1%7C1715986800000',
    '_abck': 'AD38CB75DFF7B16D1ECC276EC6459F9D~0~YAAQ03QQArC1J3qPAQAANioYjAu26PVJVtZwVmXLAmT6tESDTnyTBNHqe3NLkyNaZ4iF/27guejuXoEnEpNM4VUcKy7VvydFbtWeIuk/rXUhLm5snNosBO1zX8NOehlTPYNHQPZoW3W769kgltGbher+NP06JkaeNRj9TidJ7QeGLOAFvimwJnQ/SLet4J70T3bNT+7TS0MFmrxM6/K+d0W75Xoa2dv4nVD434/4n5qezQbjbLa74+/Jz3bU3t4AD9zGgND8ZETnlFmEr4H+IFJ9mceyR+esgR6W2FuhAD/OZoDX2n5Md26/LJuN1C4BdK1AF8iHpffwBsVtpD/eyQpRQBnFH15Nk5eqj/GHLPNEMvJ1FSAYToZ9thmgnDpwXWg6RfAlqssKE0mqfGStIIcfihK1KP6C12U=~-1~||0||~-1',
    '_scid_r': '64d92825-a826-401e-81bd-d2a80c1aed32',
    '_uetsid': '80349360152211ef9e038785c4ca1fc7',
    '_uetvid': '8034e120152211ef9c56abb562d04f54',
    'pixlee_analytics_cookie_legacy': '%7B%22CURRENT_PIXLEE_USER_ID%22%3A%2298ea454f-c1d0-2734-bc03-1a14009b2cad%22%2C%22TIME_SPENT%22%3A84%2C%22BOUNCED%22%3Afalse%7D',
    'ITXSESSIONID': '99f0e3d04395843c17cb821b5b502393',
    'BSKSESSION': 'af4635e60853df2413aeaa8536e54911',
    'bm_mi': '39BA4FEA154364F73A6366E9E1FA29FE~YAAQy3QQAlK4ZnqPAQAAvp6ljBd9VCuH86g9MOOCRs80t+lgf89giYGpCkud3jvAVtkAsA85C1T4563w4rVQZyOKN2DaCc0WMU49LEVZP6Hdw9sRsBtmRnoDn3f7NaJla+jemXX6lNP/ibyeEFBqXQVeLkWhikN0+UZi+UU7vkCAk/AHIG2NSbmlGQTikI4AtZRvMaPxK2RmCFHOxAkHICsSS38HFfAcg0IefJnXcZRoqsz5UhsWG50MGrR6uu27oRTFENW0PTn6rs4hxdm576pcZXHHKhoANH6XdcBSRexORq0D57St+IZfqRMNOowBlC2mxZ7hKI2NkQ==~1',
    'ak_bmsc': '8EC2B73020CE45249C410256056DB4AF~000000000000000000000000000000~YAAQy3QQAhvcZnqPAQAAbrymjBcSclZLaN1jhV8Zat3OcEZDibe6AyPt08iGKDyyDhU42EfdzDGMzKh8MPhv6xu0l1MolazM/2G9eACPxlcPsLWWODEK6DEcCGYT/JXHRN1iT7ItDW2zzio/cKPobnQMgTCYKWK+OG2+Gkq3DWS8JhuR43+yPrkf4ezyjZukrITNVxg6eelJrjKhUS7zGbCQvzeayopPQ5dTd69rh7QK30hqhgrynqUOPZ3Rxorzd64L9g+s2mB4WvT6MuUY8YYeKg3Pv/Gc925swHcLWa9xVey+yHJ9pg2p4+4G0/Jy6sx8lasQOIJQl2LwJKYcox+jytqKqhuUwz4FVotEAtB6TRlHBeC12wG88h1YbCO2xXvxLqSgyBwtCdgl5AUdw3GVg6Ga6QKjBwd+PO5iFhe0bPVCqAsTCcovueHv3yTXzoEGhsneVkvqnP1/0mt+bD711vYsk4KdqkhcP1HUaLlCvqxh6gFTAtMgJT3Kkmxc2USM+4L/QasrtNUHCKAJuPOhy/rG3Gl/gpnCIqcL6DwQU6YmkImzGIy6errHmHQi8ldc+CrL7/tqtMhvfjFwABeVN/hrjRho',
    '_dycst': 'dk.w.c.ss.',
    '_dy_toffset': '0',
    'IDROSTA': '912fba4ae277:292b06b04daae88c0235018cb',
    '_gat_UA-2867307-7': '1',
    'recentSearches': '["Pontalon","Tshirt","Pantalon"]',
    'bm_sz': '48F367CD09AF4234EB83BC0310D17AEE~YAAQy3QQAvE9bXqPAQAAs8PijBek7OZNvFU+E8cFRWttM7aVtOpEbqzG3A3t5HEnkA+to4M8z0kYYdudtgt8g+bPfdQmCMg+qSZwO74O3A4qU4dnNJfYufcqtebJxiojZ34cveE2aqjyHKWkuW/OOm2I/gjv1lqZcE+tSQRBVSpqDkkfmrMLE8laAzLaGm3hnIg/sg+N2V4n6xMcf/5m4dN3+rk2RCBz8SV86hgPcaeMafoTjgMdtJHByS1wGt4O4K/hmg06BQEtgrMc0saS7D20kpvC2+r3eWrl8Y3Lfv6Y2OlDr+KBwxas1S6eEt6x2qAZMP6HvnKw/skF5g1emw6fXTs1AeGln6o2yzb1sv7olYlke8qrk0WvkDaTrksu+wLMTdteelN0v1nIQ16toMkpYmbzR1z23OgWun+WYbUFoGxpa9b24BcgvIPE/eLeXuLKztwnLbwEvJfan+f1sTsCmjGPQYpu4LT8mNXFwEmGWX95+AQJZQrG10XBoX7aNAwf9FoIQzSpVFsTBaGgO58HgUmEAHFpSforG+DYq0N8K5yMDPenmoidgkKRFH/4CM9Dxr/mNUu9cQ==~4604215~3617858',
    '_ga_NOTFORGA4TRACKING': 'GS1.1.1716054677.7.1.1716055623.0.0.958116268',
    '_ga': 'GA1.1.278193432.1709215063',
    '_ga_3W4Z1T7RNM': 'GS1.1.1716054384.7.1.1716055623.48.0.0',
    '_dy_soct': '1073559.1201505.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1073852.1202092.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1042014.1095950.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1031836.1063512.1716055625',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+May+18+2024+19%3A07%3A06+GMT%2B0100+(heure+normale+d%E2%80%99Afrique+de+l%E2%80%99Ouest)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=675f91bc-6459-4817-a307-d1e20b7794d2&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=DZ%3B16&AwaitingReconsent=false',
    'OptanonAlertBoxClosed': '2024-05-18T18:07:06.366Z',
    '_ALGOLIA': 'anonymous-7ab15b0d-b137-443a-ad90-2998a114b83d',
    'TS01a8c9e3': '019ceafdc36d898c0d3ca82e4e42cd226ebc7070159a7c57f5f880b57f9916792d6b94b6e7618b1c652d9e5faca1401fb2914a646d',
    'bm_sv': '10648DEE5C49B738CD6E6F8D3A8E3BED~YAAQy3QQAjlAbXqPAQAAh9bijBdLXhYw1wXKUkaV4VqzZ3YafmZsClAU33tuE+pWH0c/vQSoG0NeFrXucjppejH8jJfeCkpQ5YT3UV2nigYUbzIlcHhV83CKLDfay4YvF0rcKwmEGG8BHOFWKrDn15x8qgVbwmQBghumAHWOMBjxUFk7dhBhRSYyhy6GN61gK4MoO/evbcvkEepmwVyru/zqPUWsFA1WW9/gPulAmRkh/caOtWwpdpaN/8jBDy7F2Qbm~1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'fr,fr-FR;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'FPID=FPID2.2.IaeNNYUwGhFnJMwISW2QP1VnWSDFarz1fjaPGLbn1Fg%3D.1709215063; optimizelyEndUserId=oeu1709215070141r0.23047570243215176; _gtmeec=e30%3D; _fbp=fb.1.1709215073593.1194989933; FPC=id=e5950294-3cce-4fba-abd8-bccac08d4e49; BershkaGenderCategoryKey=BERSHKA_MAN; _dyjsession=xzx6j0o9rf4ekxju0txoau0qvwqstfc6; dy_fs_page=www.bershka.com%2Ffr%2Fh-man.html; _dy_csc_ses=xzx6j0o9rf4ekxju0txoau0qvwqstfc6; _dy_c_exps=; _dy_c_att_exps=; _gid=GA1.2.861255091.1716042332; _dycnst=dg; _dyid=-3404720367395107493; _dy_geo=DZ.AF.DZ_34.DZ_34_; _dy_df_geo=Algeria..; FPLC=z80KxOPh1zi2mPCJN2hu9emK7i8Zxioe0dfavBDd1lBUVCGclXP1OQ04pHSAIjQZlZHzC5f94DXPppoAwpJpzUIqdt6CvaQi8f3SJOVSBKFoYOS1SEsHWihkbQk9bQ%3D%3D; _scid=64d92825-a826-401e-81bd-d2a80c1aed32; _tt_enable_cookie=1; _ttp=UbQeyBRVBQiWwgG_mdgdEgI5m2t; _sctr=1%7C1715986800000; _abck=AD38CB75DFF7B16D1ECC276EC6459F9D~0~YAAQ03QQArC1J3qPAQAANioYjAu26PVJVtZwVmXLAmT6tESDTnyTBNHqe3NLkyNaZ4iF/27guejuXoEnEpNM4VUcKy7VvydFbtWeIuk/rXUhLm5snNosBO1zX8NOehlTPYNHQPZoW3W769kgltGbher+NP06JkaeNRj9TidJ7QeGLOAFvimwJnQ/SLet4J70T3bNT+7TS0MFmrxM6/K+d0W75Xoa2dv4nVD434/4n5qezQbjbLa74+/Jz3bU3t4AD9zGgND8ZETnlFmEr4H+IFJ9mceyR+esgR6W2FuhAD/OZoDX2n5Md26/LJuN1C4BdK1AF8iHpffwBsVtpD/eyQpRQBnFH15Nk5eqj/GHLPNEMvJ1FSAYToZ9thmgnDpwXWg6RfAlqssKE0mqfGStIIcfihK1KP6C12U=~-1~||0||~-1; _scid_r=64d92825-a826-401e-81bd-d2a80c1aed32; _uetsid=80349360152211ef9e038785c4ca1fc7; _uetvid=8034e120152211ef9c56abb562d04f54; pixlee_analytics_cookie_legacy=%7B%22CURRENT_PIXLEE_USER_ID%22%3A%2298ea454f-c1d0-2734-bc03-1a14009b2cad%22%2C%22TIME_SPENT%22%3A84%2C%22BOUNCED%22%3Afalse%7D; ITXSESSIONID=99f0e3d04395843c17cb821b5b502393; BSKSESSION=af4635e60853df2413aeaa8536e54911; bm_mi=39BA4FEA154364F73A6366E9E1FA29FE~YAAQy3QQAlK4ZnqPAQAAvp6ljBd9VCuH86g9MOOCRs80t+lgf89giYGpCkud3jvAVtkAsA85C1T4563w4rVQZyOKN2DaCc0WMU49LEVZP6Hdw9sRsBtmRnoDn3f7NaJla+jemXX6lNP/ibyeEFBqXQVeLkWhikN0+UZi+UU7vkCAk/AHIG2NSbmlGQTikI4AtZRvMaPxK2RmCFHOxAkHICsSS38HFfAcg0IefJnXcZRoqsz5UhsWG50MGrR6uu27oRTFENW0PTn6rs4hxdm576pcZXHHKhoANH6XdcBSRexORq0D57St+IZfqRMNOowBlC2mxZ7hKI2NkQ==~1; ak_bmsc=8EC2B73020CE45249C410256056DB4AF~000000000000000000000000000000~YAAQy3QQAhvcZnqPAQAAbrymjBcSclZLaN1jhV8Zat3OcEZDibe6AyPt08iGKDyyDhU42EfdzDGMzKh8MPhv6xu0l1MolazM/2G9eACPxlcPsLWWODEK6DEcCGYT/JXHRN1iT7ItDW2zzio/cKPobnQMgTCYKWK+OG2+Gkq3DWS8JhuR43+yPrkf4ezyjZukrITNVxg6eelJrjKhUS7zGbCQvzeayopPQ5dTd69rh7QK30hqhgrynqUOPZ3Rxorzd64L9g+s2mB4WvT6MuUY8YYeKg3Pv/Gc925swHcLWa9xVey+yHJ9pg2p4+4G0/Jy6sx8lasQOIJQl2LwJKYcox+jytqKqhuUwz4FVotEAtB6TRlHBeC12wG88h1YbCO2xXvxLqSgyBwtCdgl5AUdw3GVg6Ga6QKjBwd+PO5iFhe0bPVCqAsTCcovueHv3yTXzoEGhsneVkvqnP1/0mt+bD711vYsk4KdqkhcP1HUaLlCvqxh6gFTAtMgJT3Kkmxc2USM+4L/QasrtNUHCKAJuPOhy/rG3Gl/gpnCIqcL6DwQU6YmkImzGIy6errHmHQi8ldc+CrL7/tqtMhvfjFwABeVN/hrjRho; _dycst=dk.w.c.ss.; _dy_toffset=0; IDROSTA=912fba4ae277:292b06b04daae88c0235018cb; _gat_UA-2867307-7=1; recentSearches=["Pontalon","Tshirt","Pantalon"]; bm_sz=48F367CD09AF4234EB83BC0310D17AEE~YAAQy3QQAvE9bXqPAQAAs8PijBek7OZNvFU+E8cFRWttM7aVtOpEbqzG3A3t5HEnkA+to4M8z0kYYdudtgt8g+bPfdQmCMg+qSZwO74O3A4qU4dnNJfYufcqtebJxiojZ34cveE2aqjyHKWkuW/OOm2I/gjv1lqZcE+tSQRBVSpqDkkfmrMLE8laAzLaGm3hnIg/sg+N2V4n6xMcf/5m4dN3+rk2RCBz8SV86hgPcaeMafoTjgMdtJHByS1wGt4O4K/hmg06BQEtgrMc0saS7D20kpvC2+r3eWrl8Y3Lfv6Y2OlDr+KBwxas1S6eEt6x2qAZMP6HvnKw/skF5g1emw6fXTs1AeGln6o2yzb1sv7olYlke8qrk0WvkDaTrksu+wLMTdteelN0v1nIQ16toMkpYmbzR1z23OgWun+WYbUFoGxpa9b24BcgvIPE/eLeXuLKztwnLbwEvJfan+f1sTsCmjGPQYpu4LT8mNXFwEmGWX95+AQJZQrG10XBoX7aNAwf9FoIQzSpVFsTBaGgO58HgUmEAHFpSforG+DYq0N8K5yMDPenmoidgkKRFH/4CM9Dxr/mNUu9cQ==~4604215~3617858; _ga_NOTFORGA4TRACKING=GS1.1.1716054677.7.1.1716055623.0.0.958116268; _ga=GA1.1.278193432.1709215063; _ga_3W4Z1T7RNM=GS1.1.1716054384.7.1.1716055623.48.0.0; _dy_soct=1073559.1201505.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1073852.1202092.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1042014.1095950.1716045964.xzx6j0o9rf4ekxju0txoau0qvwqstfc6*1031836.1063512.1716055625; OptanonConsent=isGpcEnabled=0&datestamp=Sat+May+18+2024+19%3A07%3A06+GMT%2B0100+(heure+normale+d%E2%80%99Afrique+de+l%E2%80%99Ouest)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=675f91bc-6459-4817-a307-d1e20b7794d2&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=DZ%3B16&AwaitingReconsent=false; OptanonAlertBoxClosed=2024-05-18T18:07:06.366Z; _ALGOLIA=anonymous-7ab15b0d-b137-443a-ad90-2998a114b83d; TS01a8c9e3=019ceafdc36d898c0d3ca82e4e42cd226ebc7070159a7c57f5f880b57f9916792d6b94b6e7618b1c652d9e5faca1401fb2914a646d; bm_sv=10648DEE5C49B738CD6E6F8D3A8E3BED~YAAQy3QQAjlAbXqPAQAAh9bijBdLXhYw1wXKUkaV4VqzZ3YafmZsClAU33tuE+pWH0c/vQSoG0NeFrXucjppejH8jJfeCkpQ5YT3UV2nigYUbzIlcHhV83CKLDfay4YvF0rcKwmEGG8BHOFWKrDn15x8qgVbwmQBghumAHWOMBjxUFk7dhBhRSYyhy6GN61gK4MoO/evbcvkEepmwVyru/zqPUWsFA1WW9/gPulAmRkh/caOtWwpdpaN/8jBDy7F2Qbm~1',
    'priority': 'u=1, i',
    'referer': 'https://www.bershka.com/',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
}

params = {
    'productIds': product_ids,
    'languageId': '-2',
}

url = 'https://www.bershka.com/itxrest/3/catalog/store/45009589/40259544/productsArray'

response = requests.get(
    'https://www.bershka.com/itxrest/3/catalog/store/45009589/40259544/productsArray',
    params=params,
    cookies=cookies,
    headers=headers,
)



def product_struct():
    """
    Defines the structure of product data.

    Returns:
        dict: Dictionary representing the structure of product data.
    """
    return {
        
        "product_id": "",
        "img": "",
        "name": "",
        "sectionName": "",
        "availability":"",
        "price": "",
        "oldPrice": "",
        "link": "",
        "websiteId": ""
    }


def fetch_page_data(url, params):
    """
    Fetches data from a URL using GET requests and saves it to a JSON file.

    Args:
        url (str): The URL to fetch data from.
        params (dict): Parameters to include in the request.

    Returns:
        list: List of product data dictionaries.
    """
    product_list = []
    status_code = None

    while status_code != 200:
        response = requests.get(url, params=params, headers=headers)
        status_code = response.status_code
        print("status_code: ", status_code)

    print("status_code: ", status_code)

    file_path = "page_breshka.json"

    with open(file_path, 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

    data = response.json()

    results = data["products"]
    # print(results)
    for row in results:
        
            product = product_struct()
            
            product_id = row["id"]
            product_availability = row["availabilityDate"]
            product_name = row["name"]
            product_price = row["bundleProductSummaries"][0]["detail"]["colors"][0]["sizes"][0]["price"]
            product_sectionName = row["sectionNameEN"]
            if "oldPrice" in row["bundleProductSummaries"][0]["detail"]["colors"][0]["sizes"]:
                product_oldPrice = row["bundleProductSummaries"][0]["detail"]["colors"][0]["sizes"][0]["oldPrice"]
               
            else:
                product_oldPrice = None 
        
            img_path = row["bundleProductSummaries"][0]["detail"]["xmedia"][-1]["xmediaItems"][-1]["medias"][-1]["extraInfo"]["url"]
            img_based_link = "https://static.bershka.net/4/photos2"
            product_img_link = ''.join([img_based_link, img_path] )
            
            
            product["product_id"] = product_id
            product["availability"] = product_availability
            product["name"] = product_name
            product["price"] = product_price
            product["oldPrice"] = product_oldPrice  
            product["sectionName"] = product_sectionName
            product["img"] = product_img_link
            product["link"] = product_link
            product["websiteId"] = 3
        
            
    cpt = 0
    print("size : ", len(results))
    

fetch_page_data(url , params)
    
