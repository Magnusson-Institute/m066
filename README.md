# m066

NLP experimentation (FOSS). Results are used by https://privacy.news

(Note: this repo used with external collaborators, this is free open source only, nothing proprietary etc)

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

_(Yeah the m1 boxes is what @psm prefers, you're on your own on windows or linux,
but it should be easier if anything)_

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

Currently it produces the following for the ref model (Sample 1):

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


## Problemshooting

In the end I needed a number of sources:

* https://github.com/huggingface/transformers/issues/3539
* https://developer.apple.com/metal/tensorflow-plugin/

## Future things to look at

This requires a lot of more space:

* https://github.com/kamigaito/SLAHAN



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

## Sample 3

### Baseline:

```
A Financial Times report seems to argue that Apple has allowed app
developers to collect customer data from iPhone users without their
permission.

When privacy…isn’tApple’s decision to introduce App Tracking Privacy
controls generated lots of controversy and considerable pushback from
Facebook.

It does also say that while Apple hasn’t responded to questions, it
has said privacy “remains its North Star."

It may be time for Apple to make a symbolic example to illustrate just
how serious it is about privacy.

It’s time to police the privacy promise of apps distributed via the
App Store.
```

### XLNET

```
A Financial Times report seems to argue that Apple has allowed app
developers to collect customer data from iPhone users without their
permission. Examples of user or device data include, but are not
limited to: properties of a user’s web browser and its configuration,
the user’s device and its configuration, the user’s location, or the
user’s network connection. The loophole is that services such as Snap
and Facebook have changed the way they gather data to create
anonymized groups of users, rather than to identify individuals. We
know the battle for privacy — like security — is an eternal one. Smash
their system

I think the loophole used here contravenes the spirit and expectation
of Apple’s rule, that this data “may not be combined with other data
to track a user across apps and websites owned by other companies
unless you have been granted permission to track by the user.” This
strongly suggests it reserves the right to punish developers who go
against the spirit of that deal. It wouldn’t be the first time Apple
threatened to kick Facebook out. It last did so after it was found
that domestic slaves were being sold on Facebook’s Instagram
service. It may be time for Apple to make a symbolic example to
illustrate just how serious it is about privacy.
```

## Setup (alg002)

_Warning: the data set that will be downloaded for the various models
in alg002 amount to 6 ~GB or more_

These algorithms use much bigger models - but I don't know how to run
them yet .. either gives worse results, or they break.

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
even sharing it with others. The NBC4 I-Team talked to a privacy
expert about the settings you might want to have in place to keep your
personal information as private as possible. Facebook, Amazon, Venmo
and Google are the apps and websites that most of us are using, and
those are the ones gobbling up our data. Expert Hayley Kaplan says a
quick privacy checkup will help protect some of your personal data
. Here are tips for adjusting your settings for your Amazon account
and your Venmo account. For Facebook, you may have noticed that ads
pop up based on what you’re searching for online, and you can stop the
social media giant from targeting
```

_The above needed some sentence punctuation fixds._


_breaks on sample 2_

### Results - test04d()

_Currently breaks on both samples_


### Results - Forefront.ai

_This requires an account and access to their "summarize" model,
code is in alg003, you will need a model key._


Sample 1:

```
The NBC4 I-Team talked to a privacy expert about the settings people
might want to have in place to keep their personal information as
private as possible. The apps and websites that people are using are
gobbling up the data. Hayley Kaplan is an online privacy
expert. Kaplan says a quick privacy checkup will help protect some of
your personal information. Amazon is a company that sells books and
other products online. Kaplan says if you have a wish list, it
defaults to a public setting. The quick fix for the Facebook post is
to set it to private. Now, your browsing and purchase history aren't
public. The family members can see all the information on the
Internet. The seller doesn't want someone in the family to know that
he's ordered something. Kaplan says there is a way to hide
that. Amazon tips for keeping the account private. The default setting
of Venmo is public. The payment to a therapist is private if
adjusted. Kaplan says you should hide your past transactions and your
contacts. The tips for adjusting the Venmo privacy settings are
mentioned. Kaplan prefers Zelle to other cash apps. Kaplan says the
app is highly encrypted and there is no sharing. Then he talks about
other apps. The social media giant Facebook allows people to stop it
from targeting ads at them by tweaking its settings. Kaplan suggests
not letting people tag him in posts without his approval. The text
advises people to check their Facebook settings often. Kaplan says
it's difficult to write an article about Facebook because the settings
keep changing. The place where people manage their Facebook privacy. A
Facebook privacy checkup is mentioned. Google knows everything about
everyone. Kaplan suggests not allowing the tech giant to track your
browsing history. The text tells how to access and change the Google
privacy settings. Kaplan can walk you through how to blur your home on
Google maps. Kaplan suggests not using the Google or Facebook account
to sign in to websites. Kaplan thinks education is the best
ammunition. The author thinks that once people decide that they care
about privacy, they can achieve a decent level for themselves.
```

_The above needed some polish. First of all the phrase 'The quick fix
for the Facebook post is to set it to private.' was repeated (many
times), and some other junk ('Posted by Admin on July 17, 2017 in
News.').  And it ended with the phrase 'A short summary of the
following text.'._

Sample 3:

```
A Financial Times report seems to argue that Apple has allowed app
developers to collect customer data from iPhone users without their
permission. The new version of Android will allow users to decide
whether an application can track their online activity. The Internet
has become more private and secure.  The theory is that this denies
companies that make their money collecting, curating, and selling your
information the right to track what you do online. Apple has permitted
some developers to exploit a loophole in the system. The loophole is
used by some people to get rid of the rules. The report claims
Facebook and Snapchat are exploiting a loophole in Apple's guidelines
to track users. Apple Developer guidelines specific to fingerprinting
and other technologies designed to identify a device or user say: “Per
the Apple Developer Program License Agreement, you may not derive data
from a device for the purpose of uniquely identifying it. The examples
of user or device data include a user's web browser and its
configuration, the user's device and its configuration, the user's
location, or the user's network connection. Apple has banned apps from
collecting personal information. However, some companies have found a
loophole. They still collect your information but do not share
it. Apple collects signals from an iPhone at a group level to target
cohorts of users. Personal data is anonymized. Sheryl Sandberg says
Facebook is rebuilding its ad infrastructure. Target doesn't keep
information about their online shopping habits. One rule to ring them
all though it doesn't work like that. The MIT Technology Review report
gives a terrifying insight into how even anonymized data can be
exploited to build substantial quantities of information about
people. The surveillance capitalists will turn any amount of
information into actionable data. The people who purchase the data
often use AI to develop stacks of information about you. Target
shoppers will receive ads personalized to them even though they've
asked not to be tracked. Though no one — technically — broke the
rules, everyone had a good time. A lull in an ongoing war. Apple
believes the best way to protect people's data is not to gather it in
the first place. It has made privacy a pillar to its product
offering. The battle for privacy - like the battle for security - is
an eternal one. Apple improves it and others will undermine it. The
lack of regulation is the reason for the high price of
cigarettes. Smash their system says that the loophole used by Apple to
collect data violates the spirit and expectation of Apple's
rule. Apple should intensify its privacy protections. Apple will warn
developers of future enforcement against bending of its rules at
WWDC. Apple's prohibition cites its Developer Program License
Agreement. The company reserves the right to punish developers who go
against the spirit of the deal. The author thinks there should be
consequences for companies that choose to undermine end user
protection. Apple may unfriend Facebook. Apple may threaten to kick
Facebook out of its iPhone. It was found that domestic slaves were
being sold on Facebook's Instagram service. Apple may boot Facebook
from its servers for undermining the spirit of its developer
agreement. Apple is turning a blind eye to the fact that some sellers
are selling used iPhones with fake IMEI numbers. Apple has said
privacy remains its North Star. My feeling is happy. Apple may make a
symbolic example to illustrate how serious it is about privacy. The
company will punish those who transgress the spirit of its developer
agreement. It's time to police the privacy promise of apps distributed
via the App Store. AppleHolic recommends people to follow him on
Twitter and join some groups on MeWe.
```

_Also had a trailing sentence above._