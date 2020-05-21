# box-test
Basic testing framework that prints beautiful errors.

![](example.png)

```
from boxtest import Tester

async def myAsyncTest(text):
    print('foo')
    print(text)

def mySyncTest(framework):
    print('Whats the best testing framework?')

    if framework.lower() == 'boxtest':
        print('boxtest is correct!')
    else:
        raise Exception('Wrong!')

if __name__ == '__main__':
    tester = Tester()

    tester.addAsyncTest(myAsyncTest('bar'))
    tester.addSyncTest(framework, 'unittest')
    tester.addSyncTest(framework, 'boxtest')

    tester.run()
```
