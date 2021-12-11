# m066

NLP experimentation (FOSS)

(Note: used with external collaborators)

## Setup (alg001)

On MacPro/m1 (arm64) you'll need:

```
# basic packages
brew install cmake pkg-config google-perftools
# build
cd ~/dev
git clone https://github.com/google/sentencepiece.git 
cd sentencepiece
mkdir build
cd build
cmake ..
make -j $(nproc)
sudo make install
sudo update_dyld_shared_cache  # ... this is macOs/m1 command ... deprecated?
# sudo ldconfig -v  # ... this is ubuntu command
```

Read more: https://github.com/google/sentencepiece

Then you can set up the Python environment:

```
python3.9 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
python -i ./alg001.py
```

Then inside python:

```
# reference (Newspaper3K)
test00()
# XLNET model (first time it runs will take a bit of time)
test01()
```

Currently it produces the following for the ref model:

```
“In most cases you’re just making all of your information public in
one way or another,” said online privacy expert Hayley Kaplan.

“You’re making it so easy for people to know so much about you.”But
Kaplan says a quick privacy checkup will help protect some of your
personal information.

And whatever changes you make to your Facebook settings, be sure to
check them often.

And you can also do a Facebook privacy checkup.

Here’s how to access and change your Google privacy settings.
```

And the following for the XLNET model:

```
Popular apps and websites, such as Facebook and Amazon, that many of
us use all the time, are gathering a lot of information about us, and
even sharing it with others. So the NBC4 I-Team talked to a privacy
expert about the settings you might want to have in place to keep your
personal information as private as possible. “In most cases you’re
just making all of your information public in one way or another,”
said online privacy expert Hayley Kaplan. “ And whatever changes you
make to your Facebook settings, be sure to check them often. Kaplan
suggests you don’t allow the tech giant to track your browsing
history. Here’s how to access and change your Google privacy settings.
```

Note that to add new files, you bootstrap body text through N3K:

```
test01(test00a('sample_webpages/sample_002.html').text)
```

where test00a() returns the Article() body from the sample file.

## Sample 2

### Baseline:

```
He laid out ways the company is aiming to solve it, while pointing to
trade-offs between making VR spaces safe and not policing people's
private conversations.

I don't think there is a technical limitation that prevents us from
doing more.

I don't think anyone's proposing we take these to their extremes.

The more [social VR spaces] are policed, the less privacy you're
fundamentally able to ensure that people have.

I don't think this is the kind of thing that can wait.
```

### XLNET:

```
That\'s a question Meta, the company formerly known as Facebook, has
been grappling with for some time. The tenor of the post [is]
overstated and misinformed," Bosworth said. Locally, on your device,
totally private and secure, [you] have a little rolling buffer of
what\'s the activity that happened. And we feel good about what that
represents from a standpoint of a privacy integrity trade-off, because
it\'s keeping the incidents private until somebody chooses of their
own volition to say, "This is a situation that I want to raise
visibility to." I don\'t think there is a technical limitation that
prevents us from doing more. We\'re just trying to strike a trade-off
between the privacy and the integrity challenges. You\'ve been saying
that you want to put privacy first when building new products for
Meta. But, you know, even my friends say mean things to me
sometimes. There are tools that we can build — APIs, SDKs — that
developers will be able to integrate. As we move toward a metaverse
world, what role will platform providers play in enforcing those
rules? Right now, there seem to be two blueprints: game consoles,
where companies have very strict safety requirements, and mobile
platforms, where a company like Apple doesn\'t tell app developers how
to do moderation.
```

## Setup (alg002)

_Warning: the data set that will be downloaded for the various models
in alg002 amount to 6 ~GB or more_

```
# run all algs
# 'a' will download ~1.5GB first time it runs
print("t5-base")
test04a()
# 'b' will download ~3GB first time it runs
print("t5-base (variation)")
test04b()
print("HuggingFace")
test04c()
# 'd' will download ~1.2GB first time it runs
print("gpt2")
test04d()
```


### Results - test04a()

Sample 1:

```
<pad> the NBC4 I-Team talked to a privacy expert about the settings
you might want to have in place to keep your personal information as
private as possible. for Venmo users, the default setting is public,
meaning people can see who you’re paying and when. for facebook, you
may have noticed that ads pop up based on what you’re doing.</s>
```

Sample 2:

```
"spoiler alert: I did not have a good time," an employee says of
harassment. "we have [to strike] a pretty tough balance between
privacy and integrity," he says. "we can have someone not appear to
exist to you," he says. "we can have someone not appear to exist to
you," he says.</s>'
```

### Results - test04b()

_Currently breaks on both samples_

### Results - test04c()

Sample 1:

```
Facebook and Amazon are gathering a lot of information about us, and
even sharing it with others . The NBC4 I-Team talked to a privacy
expert about the settings you might want to have in place to keep your
personal information as private as possible . Facebook, Amazon, Venmo
and Google are the apps and websites that most of us are using, and
those are the ones gobbling up our data . Expert Hayley Kaplan says a
quick privacy checkup will help protect some of your personal data
. Here are tips for adjusting your settings for your Amazon account
and your Venmo account . For Facebook, you may have noticed that ads
pop up based on what you’re searching for online, and you can stop the
social media giant from targeting
```

_breaks on sample 2_

### Results - test04d()

_Currently breaks on both samples_


