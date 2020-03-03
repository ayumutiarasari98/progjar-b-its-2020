import logging
import requests
import os
import threading



def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    for i in range(4):
        url = {}
        url[0] = "http://cdn.sci-news.com/images/enlarge7/image_8132e-COVID-19.jpg"
        url[1] = "http://theindependent.sg/wp-content/uploads/2020/02/COVID-19-update-for-Feb-13.png"
        url[2] = "https://globalbiodefense.com/wp-content/uploads/2020/02/covid-19-coronavirus-biosurveillance-epidemiology-lshtm-map.jpg"
        url[3] = "https://globalbiodefense.com/wp-content/uploads/2020/02/coronavirus-covid-19-sars-cov-2-feb-2020.jpg"
        t = threading.Thread(target=download_gambar, args=(url[i],))
        t.start()