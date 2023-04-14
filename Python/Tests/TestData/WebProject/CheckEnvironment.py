if __name__ == '__main__':
    import sys, os
    with open(sys.argv[-1], 'w') as f:
        for k in ('FOB', 'OAR', 'BAZ'):
            f.write(f'{k}={os.environ[k]}' + '\n')
