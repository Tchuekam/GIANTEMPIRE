---
id: faq
title: FAQ
description: Answers to common questions about TchueKAM Agent — pricing, privacy, data storage, updates, and supported platforms.
sidebar_position: 9
---

import Head from '@docusaurus/Head';

<Head>
  <script type="application/ld+json">
    {JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      'mainEntity': [
        {
          '@type': 'Question',
          'name': 'What is TchueKAM Agent?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'TchueKAM is a native desktop AI assistant. It runs as a real application on your computer (not in a browser tab) and helps you work with text, code, and files using AI.'}
        },
        {
          '@type': 'Question',
          'name': 'Is TchueKAM free?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'Yes. TchueKAM is free to download and use.'}
        },
        {
          '@type': 'Question',
          'name': 'Does TchueKAM work offline?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'TchueKAM needs an internet connection for AI responses and updates. Your locally stored data (conversations, settings) works offline.'}
        },
        {
          '@type': 'Question',
          'name': 'Where is my data stored?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'On your computer — Windows: %AppData%\\TchueKAM, macOS: ~/Library/Application Support/TchueKAM, Linux: ~/.config/TchueKAM. Nothing is uploaded unless you explicitly enable cloud sync.'}
        },
        {
          '@type': 'Question',
          'name': 'Does TchueKAM collect telemetry?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'TchueKAM collects anonymous usage statistics by default to help improve the product. You can opt out anytime in Settings → Privacy → Telemetry.'}
        },
        {
          '@type': 'Question',
          'name': 'What operating systems are supported?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'Windows 10 or later (64-bit), macOS 11 Big Sur or later (Intel and Apple Silicon), and Linux (Ubuntu 20.04+, Fedora 36+, or any glibc 2.31+ distro).'}
        },
        {
          '@type': 'Question',
          'name': 'Can I run TchueKAM in my company?',
          'acceptedAnswer': {'@type': 'Answer', 'text': 'Yes. TchueKAM is suitable for business use. For privacy-sensitive environments, turn off telemetry and conversation sync in Settings.'}
        }
      ]
    })}
  </script>
</Head>

# Frequently Asked Questions

## What is TchueKAM Agent?
TchueKAM is a native desktop AI assistant. It runs as a real application on your computer (not in a browser tab) and helps you work with text, code, and files using AI.

## Is TchueKAM free?
Yes. TchueKAM is free to download and use.

## Does TchueKAM work offline?
TchueKAM needs an internet connection for AI responses and updates. Your locally stored data (conversations, settings) works offline.

## Where is my data stored?
On your computer, in:
- **Windows:** `%AppData%\TchueKAM`
- **macOS:** `~/Library/Application Support/TchueKAM`
- **Linux:** `~/.config/TchueKAM`

Nothing is uploaded unless you explicitly enable cloud sync.

## How do updates work?
TchueKAM checks for updates automatically every 4 hours and on startup. When a new version is found, it downloads in the background and prompts you to restart. See [Updates](updates).

## Does TchueKAM collect telemetry?
TchueKAM collects anonymous usage statistics by default to help us improve the product. You can opt out anytime in **Settings → Privacy → Telemetry**.

## Can I use TchueKAM on multiple computers?
Yes. Install on as many machines as you want. Each install is independent unless you enable conversation sync.

## What operating systems are supported?
- Windows 10 or later (64-bit)
- macOS 11 Big Sur or later (Intel and Apple Silicon)
- Linux (Ubuntu 20.04+, Fedora 36+, or any glibc 2.31+ distro)

## How do I uninstall?
- **Windows:** Settings → Apps → TchueKAM → Uninstall
- **macOS:** Drag from Applications to Trash
- **Linux:** Delete the AppImage

To also remove your data, delete the data folder listed above.

## How do I report a bug?
[Contact us](contact) with:
- Your TchueKAM version (Settings → About)
- Your operating system
- Steps to reproduce the issue
- Any error messages

## Can I run TchueKAM in my company?
Yes. TchueKAM is suitable for business use. For privacy-sensitive environments, turn off telemetry and conversation sync in Settings.

## How do I get features I want?
We listen. [Contact us](contact) or join the [community](community) to share ideas.

Don't see your question? [Reach out](contact).
