# Contributing to Stardust

First off, thanks for taking the time to contribute! Much appreciated.

The following is a set of guidelines and rules for contributing to Stardust, which is hosted in the [Stardust Repository](https://github.com/wollemat/stardust) on GitHub.

Rules are meant to be broken.
Please, do use your best judgement when to break them and when to uphold them.
Feel free to propose changes to this document as well.

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
You might know it, we adopt the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct.
By participating, you are expected to uphold this code.
Please report unacceptable behavior to [f.c.slothouber@gmail.com](mailto:f.c.slothouber@gmail.com).

## Found a Bug?

If your issue appears to be a bug, and hasn't been reported, open a new issue. Help us to maximize
the effort we can spend fixing issues and adding new features, by not reporting duplicate issues.

Providing the following information will increase the chances of your issue being dealt with quickly:

* **Overview** -
If an error is being thrown a non-minified stack trace is of great help.
* **Motivation** -
Explain why this is a bug for you.
* **System** -
Is this a problem with all browsers or operating systems or only specific ones?
* **Reproduction** -
Provide an unambiguous set of steps to reproduce the error.
* **Related** -
Has a similar issue been reported before?
* **Suggestion** -
If you can't fix the bug yourself, perhaps you can point to what might be causing the problem (line of code or commit).

## Feature or Enhancement Suggestion?

Do you have a suggestion for a new feature or enhancement?
First make sure that no closely related or even identical issue exists.
If not, then request the feature by opening a new issue.

Providing the following information will increase the chances of your issue being dealt with quickly:

Please give sufficient information regarding the requested feature.

* **Overview** -
What is it that you want?
* **Motivation** -
Why do you want this?
* **Related** -
Has a similar issue been reported before?

## Burning Question?

We are open to relevant questions and constructive discussions.
Do however, give a rigorous description.
Why do you ask this question?
What can we do to help you know?
What could we have done to avoid this question to begin with?

## Submitting an Issue

Issues are created, used and structured in a specific way in Stardust.
Nothing demanding yet apparent nonetheless.

First make sure that your issue is not already an existing one.
We want to avoid duplicate issues as much as possible.
Before continuing have a look at our [open](https://github.com/wollemat/stardust/issues) issues, our [closed](https://github.com/wollemat/stardust/issues?q=is%3Aissue+is%3Aclosed) issues and our[dropped](https://github.com/wollemat/stardust/issues?q=is%3Aissue+label%3A%22note%3A+wont+fix%22+) labeled issues as well.

Construct the tittle such that it could be used as a [commit message](#commit-messages).

[Label](#issue-labels) your issue appropriately.
At least give it a [type](#type-labels) label and a [status](#status-labels) label (queued presumably).
[Note](#note-labels) labels are optional.

Give a clear and thorough description on the new feature, the bug or question you have.
For more explanation see the specific guidelines of [filing a bug](#found-a-bug), [requesting a feature](#feature-or-enhancement-suggestion) and [asking a question](#burning-question)

## Commit Messages

A few simple hypothetical examples: `Add parallelism support`, `Fix flaky tests` & `Implement depth first search algorithm`.
A bit of aid, the sentence *"This commit will: "* `YOUR COMMIT MESSAGE` should not necessarily be grammatically correct but be logical.

Try to be as precise and as descriptive as possible.
We recognise that sometimes that is impossible or too cumbersome and a generic message might be required.
Use your best judgement.

Occasionally we notice that aggregation is needed, for instance: `Update README, CONTRIBUTING & CODE_OF_CONDUCT`.
Again, use your best judgement.
Is this actually necessary or is an overarching message constructable?
`Update README, CONTRIBUTING & CODE_OF_CONDUCT` is considered OK.
`Fix this & Implement that` is considered NOT OK and should be be split into `Fix this` and `Implement that`

Use the imperative present tense and not any 3rd-person -s or continuous -ing.
For example `Add support for ...` is OK, `Adds support for ...` is NOT OK, `Added support for ...` is also NOT OK and `Adding support for ...` is NOT OK as well.

Avoid small and little contributing words and phrases.
For instance: `a`, `an`, `as`, `the` and `for` are not desirable.
Again, exceptions may apply.

Start with a with a Capital.

DO NOT put a dot (.) at the end.

## Issue Labels

Speaking of labels, we have a few. Issues should always have 2 types of labels: a status label and a type label.

### Status Labels

There are 3 status labels:

* [Queued](https://github.com/wollemat/stardust/issues?q=label%3A%22status%3A+pending%22+) -
Not been picked up yet by anyone and is not currently tackled.
You are free to pick any you want.
Every issue starts off with this status.
* [Pending](https://github.com/wollemat/stardust/issues?q=label%3A%22status%3A+in+progress%22+) -
Actively being worked on by someone.
Perhaps check for a matching [pull request](https://github.com/wollemat/stardust/pulls).
* [Done](https://github.com/wollemat/stardust/issues?q=label%3A%22status%3A+done%22+) -
Discussion is resolved, question is answered, bug is fixed or feature is implemented.
The code is verified as well and the changes have been merged with at least the `develop` branch.
Ultimately every issue ends up with this status implemented or not.

### Type Labels

There are 4 type labels:

* [Bug](https://github.com/wollemat/stardust/issues?q=label%3A%22type%3A+bug%22+) -
Noticed a bug, error or fault when using Stardust?
File a bug report with this label.
We will attempt to fix it as soon as possible.
* [Feature](https://github.com/wollemat/stardust/issues?q=label%3A%22type%3A+feature%22+) -
Do you have a suggestion for a new feature or other enhancement?
Please let us know by creating a new issue with the details and don't forget the feature label.
* [Question](https://github.com/wollemat/stardust/issues?q=label%3A%22type%3A+question%22+) -
Looking to ask a relevant question or start a constructive discussion?
Create an issue with this label and incite that discussion or ask away in any other form.
* [Chore](https://github.com/wollemat/stardust/issues?q=label%3A%22type%3A+chore%22+) -
For anything else.
Found a typo? That is a chore.
Lacking documentation? That is a chore.
Build fails? That is a chore.

### Note Labels

In addition we have a few "note" labels:

* [Duplicate](https://github.com/wollemat/stardust/issues?q=label%3A%22note%3A+duplicate%22+) -
If an identical issue is already existing then the regarding issue is linked to in this issue.
Additionally the issue receives this label and is closed.
* [Urgent](https://github.com/wollemat/stardust/issues?q=label%3A%22note%3A+urgent%22+) -
Used if something is absolutely mission critical.
Big security risks, program breaking bugs or anything else urgent.
* [Epic](https://github.com/wollemat/stardust/issues?q=label%3A%22note%3A+epic%22+) -
Used if an issue is too large to realistically be implemented in a single commit or pull request.
The issue will most likely be split into smaller more manageable issues down the road.
* [Dropped](https://github.com/wollemat/stardust/issues?q=label%3A%22note%3A+wont+fix%22+) -
This label is given to any issue that will not be implemented, fixed, answered or simply not interacted with.
Think of out of scope discussions & questions or idiotic feature requests.
* [(╯ಠ_ಠ)╯︵ ┻━┻](https://github.com/wollemat/stardust/issues?q=label%3A%22note%3A+%28%E2%95%AF%E0%B2%A0_%E0%B2%A0%29%E2%95%AF%EF%B8%B5+%E2%94%BB%E2%94%81%E2%94%BB%22+) -
A bit of comic relief or when needing an anger outlet.
Is an issue frustrating or otherwise infuriating?
Let others know what they are getting themselves into with this label.

## Help us Fix it

* Fork the [repository](https://github.com/wollemat/stardust) or if you already forked it update your `develop` branch.
* Checkout a new branch from `develop`. Follow the branch name conventions. Use the "topic/`type`/`branch-name`" format.
DO NOT use Capitals.
Avoid digits or special characters.
Use [kebab case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles) for the branch name.
Some examples are: `topic/chore/readme`, `topic/feature/parallelism` and `topic/bug/heart-bleed`.
The only exemptions are the `master` branch, the `develop` branch, the `hotfix` branch and the `release/version` branches.
* Make your changes and commit them.
Remember the [commit message conventions](#commit-messages).
Do not forget to add yourself to the contributor section of the [README](README.md) if not done so already.
Credit where credit due.
* Push your branch to your own forked repository.
* Create a [Pull Request](https://github.com/wollemat/stardust/compare) with the our `develop` branch as base branch.
Use the same title of the issue for the pull request title and refer relevant issue(s) in the description.
* We might have some comments and might request changes.
Afterwards, if the build is successful, all the tests pass and there are no more comments then the branch can be merged.
We will do that for you.
* Bathe in the glory of contributing to a open source project and making the world a better place.

## License

<p align="center">This project and its code are released under the MIT license. Please have a look at the <a href="LICENSE.md">LICENSE.md</a> for more details.</p>
<p align="center">copyright © <a href="https://github.com/wollemat">wollemat</a></p>
