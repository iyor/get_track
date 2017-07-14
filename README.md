# get_track

A commandline tool for finding _EXACTLY_ the song you need.

## Setup

Run the following command in your terminal:

```
git clone https://github.com/iyor/get_track.git && \
cd get_track/ && virtualenv -p python3 env && \
env/bin/pip3.6 install spotipy
```

You need to set up spotify credentials according to [this guide](https://developer.spotify.com/web-api/tutorial/), after which you fill in your *client id* and *client secret* in the `env.py` file. After that you run the script with

```
env/bin/python3.6 get_track.py <DAT TRACK U NEED>
```

For certain tricky song titles, this might take a long time, but hey, it would've taken you even longer.

## Example run

```
$ env/bin/python3.6 get_track.py and

Checking for song:       and

Using the following keys: 
ID:          blablablablablablablablablablabla
Secret:      blablablablablablablablablablabla
-----------------------------------------------------------------
and  -  EDEN
spotify:track:5cIZoKmBiFgjabaBG0D9fO
```

## Dependencies
* python3
* spotipy
