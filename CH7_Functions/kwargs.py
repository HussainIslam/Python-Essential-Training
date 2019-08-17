#!/urs/bin/env python3

def main():
    kitten(Buffy = 'meow', Zilla = 'grrr', Angel = 'rawr')

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('kitten {} says {}'.format(k, kwargs[k]))
    else:
        print('Empty arguments')


if __name__ == "__main__":
    main()