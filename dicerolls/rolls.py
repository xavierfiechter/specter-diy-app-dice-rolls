from binascii import hexlify
from embit import bip39

def rolls(r):
    """
    Original file from https://coldcardwallet.com/docs/rolls.py wrapped
    into rolls(r), slightly modifed to make this work in the DIY.

    Everything else is unchanged! Trust me. ;-)

    """
    warning_message = None


    # Usag:
    #
    #   echo 123456123456 | python3 rolls.py
    #
    # - Requires python3 and nothing else!
    # - This file is <https://coldcardwallet.com/docs/rolls.py>
    # - Public domain.
    #
    from hashlib import sha256

    # Read input, remove whitespace around it
    # modifed, input is passed through wrapper function
    # r = input().strip()

    # Calc sha256
    h = sha256(r.encode()).digest()

    # Show the hash
    #print(h.hex())
    #print()

    # Sanity check for empty input
    empty = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    #if h.hex() == empty:
    #    print('WARNING: Input is empty. This is a known wallet\n')

    # Warnings for short length
    if len(r) < 99:
        ae = 2.585 * len(r)
        print('WARNING: Input is only %d bits of entropy\n' % ae)
        warning_message = 'WARNING: Input is only %d bits of entropy\n' % ae

    # Apply BIP39 to convert into seed words
    v = int.from_bytes(h, 'big') << 8
    w = []
    for i in range(24):
        v, m = divmod(v, 2048)
        w.insert(0, m)
    assert not v

    # final 8 bits are a checksum
    w[-1] |= sha256(h).digest()[0]

    # Print index number and each word (24)
    #print('\n'.join('%4d: %s' % (n+1, bip39.WORDLIST[i]) for n, i in enumerate(w)))

    # added this line to get the seed words as return value
    return (warning_message, ' '.join('%4d: %s' % (n+1, bip39.WORDLIST[i]) for n, i in enumerate(w)), w, h)
