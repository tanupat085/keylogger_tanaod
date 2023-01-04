from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        with open('log.txt','a',encoding='utf-8') as file:
            t = '{}'.format(key.char)
            file.write(t)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        with open('log.txt','a',encoding='utf-8') as file:
            t = '|{}|'.format(key)
            if key == keyboard.Key.enter :
                file.write('\n')
            file.write(t)

count = 0

def on_release(key):
    global count
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()