import ast


def snip_func(url_list):
    rtmp_urls = ast.literal_eval(url_list)
    ss = ""
    if len(rtmp_urls) != 0:
        for i in rtmp_urls:
            if ss == "":
                zz = '-map 0:0 -map 1:0 "[f=flv:flvflags=no_duration_filesize]{}"'.format(i)
                ss+=zz
            else:
                pp = "|[f=flv:flvflags=no_duration_filesize]{}".format(i)
                ss = ss[:-1] + pp + '"'

    return ss