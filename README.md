<h1 align="center">Lego Collection Tracker - Webapp</h1>

<p align="center">
    <!-- issues -->
    <img src="https://img.shields.io/github/issues/tristann3/lego-collection-xref" >
    <!-- pull requests -->
    <img src="https://img.shields.io/github/issues-pr/tristann3/lego-collection-xref" />
    <!-- number of commits per year -->
    <img src="https://img.shields.io/github/commit-activity/y/tristann3/lego-collection-xref" />
    <!-- last commit -->
    <img src="https://img.shields.io/github/last-commit/tristann3/lego-collection-xref" />
    <!-- code size  -->
    <img src="https://img.shields.io/github/languages/code-size/tristann3/lego-collection-xref" />
    <!-- image size -->
    <img src ="https://img.shields.io/docker/image-size/tristann3/legos_app_image">
    <!-- website up/down status -->
    <img src ="https://img.shields.io/website?down_color=red&down_message=down&up_color=green&up_message=up&url=https%3A%2F%2Flego-tracker.dev.tristan-thompson.com">

</p>

> <h2 align="center">Table of Contents</h2>
<ul>
  <li><h2><a href=#About> About</a></h2></li>
  <li><h2><a href=#About> How To Use</a></h2></li>
  <li><h2><a href=#About> Website Monitoring</a></h2></li>
</ul>

</br></br></br></br>

> <h2 id="About" align="center">About</h2>

Lego Tracker is a tool used by LEGO collectors to see what sets they can build with their spare parts.


In the future, We hope to develop this project so that:

- A User can cross reference a set's requirements to build a set they have not yet bought

- Create an environment that makes it effortless to add/remove parts to their collection

- Implement Test Driven Development

- Sort a user's collection based on a number of parameters

- Create a user's favorite list for sets

</br></br></br></br>

> <h2 align="center"> How To Use </h2>
</br>

<h2 align="center">Download with Docker Hub repository</h2>

```
docker pull tristann3/legos_app_image:latest
```
<h1 align="center">OR</h1>

<h2 align="center">Download with Github repository</h2>

```
docker run --name repo alpine/git clone https://github.com/tristann3/lego-collection-xref
```


<h2 align="center">Run the image as a container</h2>

```
docker run -p 5000:5000 --rm --name legos_app_container tristann3/legos_app_image:latest
```

</br></br></br></br>
> <h2 align="center">Website Monitoring</h2>
<p align="center"><a>https://tristan15thompson.freshping.io/dashboard</a></p>