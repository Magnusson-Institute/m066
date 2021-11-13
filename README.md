# m066

NLP experimentation (FOSS)

(Note: used with external collaborators)

```
python3.9 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
python -i ./alg-01.py
```

Then inside python:

```
# reference (Newspaper3K)
test00()
# XLNET model
test01()
```

Currently it produces:

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

for the reference and:

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

for the XLNET model.

Note that to add new files, you bootstrap body text through N3K:

```
test01(test00a('sample_webpages/sample_002.html').text)
```

where test00a() returns the Article() body from the sample file.

## Sample 2

Baseline:

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

XLNET:

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