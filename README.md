# m066

NLP experimentation (FOSS). Results are used by https://privacy.news

(Note: this repo used with external collaborators, this is free open source only, nothing proprietary etc)

## Setup (alg001)

Make sure you've updated brew, and have latest xcode; also make sure
to start and exit xcode so it can do any cleanup (such as command line
tools).

```
# basic packages
brew install cmake pkg-config google-perftools gcc rust cython htslib
```

Until very recently, sentencepiece needed to be installed manually (on
MacPro/m1 arm64), but regular brew install should work now. If not:

```
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
# i'm shifting towards 3.10 but 3.9 should be fine
python3.10 -m venv venv
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

And here's Forefront.ai (alg003.py):

_Compression level 2:_

```
Some popular apps and websites that many of us use are gathering a lot
of information about us, and even sharing it with others. Online
privacy is a mess. You’re a smart consumer, so you know how to protect
your privacy. If you shop on Amazon, you know your purchase history is
there for you to see. If you use Venmo to pay your bills, you might
want to think twice before sharing your payment history with your
friends. If you’re using cash apps like Venmo or Square Cash, you may
be sharing your financial information with the app’s users. Facebook
is the most popular social network, but it can be a trap for the
unwary. You can check your Facebook privacy settings here. You can get
your privacy back, says computer security expert Ted Kaplan.
```

_Compression level 3:_

```
Some of the apps and websites you use every day are gathering and
sharing your personal information. If you’re shopping online, you
might be sharing more than you realize. If you use cash apps like
Venmo or Facebook, you may want to make sure your privacy settings are
up to date. When it comes to your online privacy, it’s not always easy
to know what’s going on. You can get your privacy back, says computer
security expert Ted Kaplan.
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

### Forefront (alg003.py):

_Compression level 3:_

```
The virtual reality company that wants to give people the ability to
move their bodies in virtual space has some big challenges to
overcome. A leaked internal document from virtual reality company Meta
describes an incident in which an employee was subjected to lewd
comments in an online virtual world. What tools are you using to fight
harassment in virtual reality? When you go into Horizon, you can see
what's going on around you. We're trying to strike a balance between
privacy and integrity. When it comes to virtual reality, there are two
main concerns: privacy and safety. Facebook is working on tools that
developers can use to help keep people safe in virtual worlds. The
virtual worlds that people inhabit are often cross-platform, with
people on mobile devices, in VR headsets, on PCs and on consoles. The
virtual reality company Meta has announced plans to make safety the
top priority for its virtual reality platform.
```

_Compression level 4:_

```
The idea of virtual reality is to let people explore virtual worlds
that are in some ways like real life. When you think about virtual
reality, what comes to mind? When it comes to virtual reality, there
are two things that are really important: privacy and
safety. Microsoft is working on tools that developers can use to help
keep people safe in virtual reality and augmented reality. The virtual
reality company Meta has announced plans to make safety the top
priority for its virtual reality platform.
```

_Compression level 5:_

```
The idea of virtual reality is to let people explore virtual worlds,
but that freedom can lead to some very ugly experiences. When it comes
to fighting harassment in virtual reality, there are many challenges
that have to be overcome. The future of virtual reality is bright, and
it's all thanks to the support of its fans.
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
permission. The theory is that this denies companies that make their
money collecting, curating, and selling your information the right to
track what you do online. The loophole is that services such as Snap
and Facebook have changed the way they gather data to create
anonymized groups of users, rather than to identify individuals. We
know the battle for privacy — like security — is an eternal one. I
think the loophole used here contravenes the spirit and expectation of
Apple’s rule, that this data “may not be combined with other data to
track a user across apps and websites owned by other companies unless
you have been granted permission to track by the user.” Apple’s
prohibition cites its Developer Program License Agreement. This
strongly suggests it reserves the right to punish developers who go
against the spirit of that deal. It last did so after it was found
that domestic slaves were being sold on Facebook’s Instagram service.
```


### Forefront (alg003.py):

Compression level 3 breaks unless TEXT_3 is correct to exclude subheadings.
Note how "attribution" is lost.

_Compression level 2:_

```
Apple has been accused of letting app developers track iPhone users
without their knowledge. Apple has introduced a new feature that makes
it harder for companies that want to track your online activity to do
so. Apple has long been at pains to ensure its App Store does not
allow developers to use the devices of their users to track
them. Apple has closed a loophole that allowed companies to circumvent
its privacy rules and gather data from iPhone users. Facebook is
promising to make sure that the data it gathers about you is used only
for advertising purposes. Target is facing a class action lawsuit over
its decision to share customer data with a data analytics firm. Apple
has been accused of using its dominant position in the smartphone
market to force developers to share user data with the
company. Apple’s App Tracking controls are an important part of its
privacy protections for iPhone users. Apple has long been clear about
its position on app developers circumventing its App Store rules on
user privacy. Apple has threatened to boot Facebook from its app store
for running ads that circumvent its app developer agreement. Apple has
been accused of allowing app developers to share user data with third
parties without permission. Apple’s App Store is a treasure trove of
apps that promise to make your life easier, more fun, or more
productive.
```

_Compression level 3:_

```
Apple has introduced new App Tracking Privacy controls to give iPhone
users greater control over how their data is used by app
developers. Apple has long been at pains to ensure that apps on its
App Store do not use the company’s devices to track their
users. Facebook is promising to give users more control over how their
data is used by the company. Apple has been accused of circumventing
its own privacy rules by using a loophole to allow Facebook to track
iPhone users. Apple has long been clear that its App Store rules
prohibit advertising or marketing services that circumvent its user
privacy protections. Apple is a company that prides itself on privacy.
```

_Compression level 4:_

```
Apple has introduced App Tracking Privacy controls to give iPhone
users control over how their data is used by app developers. Apple has
introduced new privacy controls for iPhone users that allow them to
limit how their data is used by app developers. Apple has long been at
the forefront of promoting user privacy.
```

_Compression level 5:_

```
Apple has introduced new App Tracking Privacy controls to give iPhone
users more control over how their data is used. Apple has long been at
the forefront of promoting user privacy.
```

As an experiment, here's what Forefront produces when pointed at the underlying
report (on FT.com), on compression "2":

```
Apple has made a major change to how it lets app developers use data
from its iPhone users, in a move that could allow companies to track
their movements and habits without their knowledge. The Californian
consumer watchdog, the Consumer Financial Protection Bureau, last year
told companies that share data with Apple that they must first remove
all references to individual consumers. Mobile advertising companies
have found ways to circumvent Apple’s ban on tracking iPhone users by
their unique IDs. Apple’s decision to force developers to give users
the option to delete their data from its App Store is a sign that the
company is taking data privacy seriously, according to a leading app
developer. Apple has said it will allow some companies to circumvent
its strict privacy rules on third-party advertising. Apple has long
been at the forefront of mobile privacy, but new research from app
developer Adblock Plus shows that some of its most popular apps are
continuing to leak user data. The European Union’s General Data
Protection Regulation (GDPR) is designed to give consumers control
over how their data is used by companies.
```

Compression levels 4 and 5 on the the same underlying FT.com article are interesting:

```
Apple has made a subtle change to its privacy policies that could
allow companies to circumvent its efforts to shield iPhone users from
unwarranted tracking. Apple has long been a champion of user privacy,
banning third-party advertising trackers from tracking its users.
```

```
The world’s most popular smartphone maker has made it easy for
companies to circumvent its privacy rules, which are designed to
shield its users from being tracked by third parties.
```

But after some small polishing of the input text (removing extraneous
"recommended" texts to podcasts embedded in the article), levels 4 and
5 changed to:

```
Apple has made a subtle change to its privacy policies that could
allow companies to circumvent its efforts to shield iPhone users from
unwarranted tracking. Apple’s new privacy rules for iOS apps are so
broad that companies have found ways to circumvent them.
```

```
Apple has made it clear that its iPhones are not to be used as
surveillance devices.
```

In contrast, here's XLNET results for the same (FT) article:

```
Apple has allowed app developers to collect data from its 1bn iPhone
users for targeted advertising, in an unacknowledged shift that lets
companies follow a much looser interpretation of its controversial
privacy policy. Lockdown Privacy, an app that blocks ad trackers, has
called Apple’s policy “functionally useless in stopping third-party
tracking”. But the companies aggregating user-level data said the
reason apps continue to “leak” information such as a user’s IP address
and location was simply because some require such information to
function. Companies will pledge that they only look at user-level data
once it has been anonymised, but without access to the data or
algorithms working behind the scenes, users won’t really know if their
data privacy has been preserved, said Munchbach. “ It’s not
unreasonable to assume it leaves a lot to be desired.”'
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


### Results - test05a() (Forefront.ai)

_This requires an account and access to their "summarize" model,
code is in alg003, you will need a model key. At time of writing,
their pricing equates to about 15 cents per summary._

See: https://www.forefront.ai/blog-posts/how-to-summarize-text-with-ai

Sample run:

```
python -i ./alg003.py
>>> # this replicates forefront's blog posting (nytimes article)
>>> test05a()
>>> # this runs range of compression levels on specific sample texts
>>> test05a(the_text=TEXT_1, c_range=range(1,6))
>>> # this replicates the FT.com article resuls (for example)
>>> test05a(the_text=TEXT_3_FT, c_range=range(3,6))
```

Forefront reports on their blog that it should generate (sample 5):

```
The job market is great but people still prefer doing gig work
because of the flexibility. Ms. Bettis thinks that income from gigs
can help her save enough money to open her own storefront. She is one
of the many Americans who are embracing the new working style. Silvia
Valladares used Snagajob to support herself as a college student. She
took shine to hospitality and decided to make that her career. She is
now the bed-and-breakfast director.  Daniel Schneider, a professor at
Harvard Kennedy School of Government who has studied low-wage work,
says that companies using gig work as way to shift costs to workers He
thinks that people who are looking for jobs will be affected if the
economy tips into recession.
```

We got something similar at compression level "3" and "4":

```
[3] Why do people continue to do gig work when the job market is so good?
The so-called gig economy — short-term contracts for services such as
ride-sharing or delivery — is changing how people work, with more than
15 million Americans now doing so, according to data from financial
apps. The world of work is changing, with many workers finding
themselves in what are known as “gig economies” that offer short-term
contracts, low wages and flexible hours. The number of people working
in the so-called gig economy is hard to pin down. The shift from
full-time jobs to freelance work is continuing, with more workers
taking on short-term jobs that offer flexibility and low overhead. The
online labor market is changing how workers find jobs, from
freelancers to full-time employees. The rise of the so-called gig
economy, in which workers are hired on short-term contracts, has made
it a key part of the economy, with some two million workers now
employed by companies such as Uber, AirBnB and TaskRabbit. The rise of
online platforms that connect workers with customers has made it easy
for companies to hire workers on short-term contracts.
```

```
[4] The job market is strong, but many workers are turning to side gigs to
supplement their incomes. The world of work is changing, with more
people working as freelancers, or "gig workers," for companies that
hire them on short-term contracts. The shift from full-time jobs to
freelance work is changing how people earn money, from how they spend
their time to how they get paid. The rise of online platforms that
connect workers with jobs has been a boon for many low-income workers,
providing an easy way to earn extra money.
```

