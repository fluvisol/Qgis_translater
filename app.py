import translators as ts
import translators.server as tss
import polib
import glob
import io

# wyw_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
# chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'
# chs_html = '''
# <!DOCTYPE html>
# <html>
# <head>
#     <title>《季姬击鸡记》</title>
# </head>
# <body>
# <p>还有另一篇文章《施氏食狮史》。</p>
# </body>
# </html>
# '''

# ### usage
# print(ts.translators_pool)
# print(ts.translate_text(chs_text))
# print(ts.translate_html(chs_html, translator='iciba'))

# ### common parameters and functions
# ## query text
# print(ts.translate_text(chs_text, if_ignore_empty_query=False, if_ignore_limit_of_length=False, limit_of_length=5000))

# ## language
# # input language
# from_language, to_language = 'zh', 'en'
# print(tss.google(wyw_text, from_language, to_language))
# # check input language with language_map
# assert from_language in tss._google.language_map  # request once first, then

# ## detail result
# print(tss.sogou(wyw_text, is_detail_result=True))

# ## professional field
# print(tss.alibaba(wyw_text, professional_field='general'))  # ("general","message","offer")
# print(tss.baidu(wyw_text, professional_field='common'))  # ('common','medicine','electronics','mechanics')
# print(tss.caiyun(wyw_text, professional_field=None))  # (None,"medicine","law","machinery")

# ## host config
# # cn
# print(tss.google(wyw_text, if_use_cn_host=False))
# print(tss.bing(wyw_text, if_use_cn_host=True))
# # reset host
# print(tss.google(wyw_text, reset_host_url=None))
# print(tss.yandex(wyw_text, reset_host_url=None))
# # host pool
# print(tss._argos.host_pool)
# print(tss.argos(wyw_text, reset_host_url=None))

# ## request config
# print(tss.lingvanex(wyw_text, sleep_seconds=5, timeout=None, proxies=None))

# ## session update
# print(tss.itranslate(wyw_text, update_session_after_seconds=1.5e3))

# ## time stat
# print(tss.reverso(wyw_text, if_show_time_stat=True, show_time_stat_precision=4, sleep_seconds=0.1))

# ## old server
# baidu_v1 = tss.BaiduV1().baidu_api
# baidu_v2 = tss.BaiduV2().baidu_api
# print(baidu_v1(wyw_text))
# assert baidu_v2(wyw_text) == tss.baidu(wyw_text)

# ### property
# print(dir(tss._deepl))
# help(tss.papago)



# # WE
# def get_translate(text): 
#     # return tss.yandex(text, reset_host_url=None)
#     return ts.translate_text(text)

# def runByPoFile(file_path):
#     po = polib.pofile(file_path)
#     for entry in po:
    # if entry.msgid == '':
    #         continue
#         entry.msgstr = get_translate(entry.msgid)

# file_paths = glob.glob(".\SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\*")

# for file_path in file_paths:
#     runByPoFile(file_path)

# S

# for file_path in glob.glob(".\SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\*"):
#     po = polib.pofile(file_path)
#     for entry in po:
    # if entry.msgid == '':
    #         continue
#         entry.msgstr = ts.translate_text(entry.msgid)



# po = polib.pofile('SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\installation_mac.po')
# for entry in po:
#     if entry.msgid == '':
#         continue
#     # entry.msgstr = ts.translate_text(entry.msgid)
#     # print(ts.translate_text(entry.msgid, from_language, to_language))
#     print(tss.google(entry.msgid, from_language, to_language))

# input = open('SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\installation_mac.po', 'r')

# splitLen = 20         # 20 lines per file
# outputBase = 'output' # output.1.txt, output.2.txt, etc.
# count = 0
# at = 0
# dest = None
# for line in input:
#     if count % splitLen == 0:
#         if dest: dest.close()
#         dest = open(outputBase + str(at) + '.txt', 'w')
#         at += 1
#     dest.write(line)
#     count += 1

# print(f'{outputBase} {splitLen} {count} {at} {dest}')


def my_traslate(text):
    from_language, to_language = 'en', 'ru'
    return text
    # return tss.google(text, from_language, to_language)
    # return ts.translate_text(text, from_language, to_language)
    # return tss.yandex(text)

global message_id

def rewrite_file(file_name):
    with open(file_name, "r+", encoding="utf-8") as text:
        text_blocks = text.read().split('\n#:')
        for text_block in text_blocks:
            message_id = None
            messages_subs = []
            for line in text_block.split('\n')[1:]:
                if len(line) == 0: continue
                pe = line.split(maxsplit=1)
                if len(pe) >= 2:
                    [head, tail] = pe
                    if message_id == None and head == 'msgid' and tail != '""':
                        message_id = tail
                    elif head == 'msgstr' and tail == '""':
                        if message_id != None:
                            line = f'msgstr { my_traslate(message_id) }'
                        if len(messages_subs) > 0:
                            for messages_sub in messages_subs:
                                line += f'\n{ my_traslate(messages_sub) }'
                        message_id = None
                        messages_subs = []
                        print(f'>>> new line {line}')
                if line[0] == '"':
                    messages_subs.append(line)
                    
                
        # for line in lines:
        #     words = line.split(' ')
        #     if words[0] == 'msgid' and ' '.join(words[1:]) != '""':
        #         new_msgid = ' '.join(words[1:])
        #         new_msgs = []
        #     elif words[0] == 'msgstr' and new_msgid != '':
        #         line = f'msgstr {my_traslate(new_msgid)}'
        #         if len(new_msgs) > 0:
        #             for msg in new_msgs:
        #                 line += f'\n{my_traslate(msg)}'
        #         new_msgid = ''
        #         new_msgs = []
        #     elif words[0] != '' and words[0][0] == '"':
        #         new_msgs.append(line)
        #     newLines.append(line)

        text.seek(0) # rewind
        text.write('\n#:'.join(text_blocks))
        text.close()

test_file = "SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\FAQ.po"
rewrite_file(test_file)