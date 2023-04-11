# SteamChecker
This is a steam account checker that uses https / http proxies to check and store the logs into a file.

At the moment, there is still work to be done with it as it is not logging correctly but everything currently is working except sanity checks on if the log is actually valid. It can be fixed fairly easily but I just want to move on to a different project so I said I would post it.

If you don't know where to find proxies, proxyscrape has an option for a free proxylist. It isn't very good but thats what free will get you.

If you don't know where to find logs, I suggest looking around for autoshops selling them in bulk or a log seller.

## Cloning
```bash
git clone --recursive https://github.com/Kurumi2k/SteamChecker.git
```

## Dependencies
Here is the list of dependencies
- [Selenium](https://pypi.org/project/selenium/ "Selenium on Pypi")
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/ "BeautifulSoup on Pypi")

## Appreciation
Thanks to @Penetrable and @TwinTurbo on Telegram for helping me with a few issues and essentially setting my head straight to be able to get the project where it is.
