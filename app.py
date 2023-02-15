import translators as ts
import translators.server as tss
import glob

def my_traslate(text):
    from_language, to_language = 'en', 'ru'
    # return text
    return tss.google(text, from_language, to_language)
    # return ts.translate_text(text, from_language, to_language)
    # return tss.yandex(text)

def rewrite_file(file_name):
    with open(file_name, "r+", encoding="utf-8") as text:
        text_blocks = text.read().split('\n#:')
        text_blocks_new = []
        for text_block in text_blocks:
            message_id = None
            messages_subs = []
            lines = []
            for line in text_block.split('\n'):
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
                        print(line)
                if line[0] == '"':
                    messages_subs.append(line)
                lines.append(line)
            text_blocks_new.append('\n'.join(lines))
        text.seek(0) # rewind
        text.write('\n\n#:'.join(text_blocks_new))
        text.close()

# test_file = "SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\FAQ.po"
# rewrite_file(test_file)

for file_path in glob.glob(".\SemiAutomaticClassificationManual_v4\locale\\ru\LC_MESSAGES\*"):
    print(f'Starting file { file_path }')
    rewrite_file(file_path)
    print(f'End file { file_path }')
