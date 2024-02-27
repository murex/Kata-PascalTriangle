[![Gradle](https://github.com/murex/Kata-PascalTriangle/actions/workflows/gradle.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/gradle.yml)
[![Maven](https://github.com/murex/Kata-PascalTriangle/actions/workflows/maven.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/maven.yml)
[![CMake](https://github.com/murex/Kata-PascalTriangle/actions/workflows/cmake.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/cmake.yml)
[![Go](https://github.com/murex/Kata-PascalTriangle/actions/workflows/go.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/go.yml)
[![Pytest](https://github.com/murex/Kata-PascalTriangle/actions/workflows/pytest.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/pytest.yml)
[![Npm](https://github.com/murex/Kata-PascalTriangle/actions/workflows/npm.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/npm.yml)
[![Check Markdown links](https://github.com/murex/Kata-PascalTriangle/actions/workflows/markdown-link-check.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/markdown-link-check.yml)
[![Add contributors](https://github.com/murex/Kata-PascalTriangle/actions/workflows/contributors.yml/badge.svg)](https://github.com/murex/Kata-PascalTriangle/actions/workflows/contributors.yml)

# Pascal Triangle

![Animated GIF of the Pascal Triangle](images/PascalTriangleAnimated2.gif) <br>
"[PascalTriangleAnimated2](https://en.wikipedia.org/wiki/Pascal%27s_triangle)"
by [Hersfold](https://en.wikipedia.org/wiki/User:Hersfold)
in [Public Domain](https://en.wikipedia.org/wiki/Public_domain)

## Description

The goal of this kata is to generate a string version of Pascal's Triangle up to a given line. It's a nice problem to
practice a mix of top-down and bottom-up styles.

### What are Bottom-up and Top-down TDD?

Bottom-up style is when you build a brick outside your main acceptance test flow and only later integrate it
with the rest of the program. On the contrary, Top-down style is when you only work on the code that is covered
by the acceptance or high level tests.

In order to experiment full bottom-up style start the kata with 10 minutes of up-front design and come up with the
different 'bricks' you will need to solve the problem. Then use the bottom-up way to solve the kata:

1. Write an acceptance test, and comment it
2. Test drive the implementation of each brick
3. Using all the bricks, test drive the implementation of the main function
4. Uncomment and pass your acceptance test

_Note: Bottom-up / Top-down are also known as Inside-out / Outside-in_

### The pros of Bottom-up TDD?

* It lets you work in small steps
* It tends to result in more reusable and robust bricks

### The cons of Bottom-up TDD?

* There is a risk that the brick does not integrate well with the main code, leading to a lot of rework. Then a good recommendation is to integrate the brick as soon as possible in the main code.
* Creating a robust brick is often more work than necessary for the current acceptance test

## Getting Started

- [C++](cpp/GETTING_STARTED.md)
- [Go](go/GETTING_STARTED.md)
- [Java](java/GETTING_STARTED.md)
- [Python](python/GETTING_STARTED.md)
- [Typescript](typescript/GETTING_STARTED.md)

## Session Quick Retrospective

You can fill it from [here](QuickRetrospective.md)

## Useful Links

### For this Kata

- [Wikipedia page on Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- [TDD - From the Inside Out or the Outside In?](https://8thlight.com/blog/georgina-mcfadyen/2016/06/27/inside-out-tdd-vs-outside-in.html) by Georgina McFadyen

### General

- [TCR (Test && Commit || Revert) wrapper](tcr/TCR.md) utility
- Collaborative timer for pairing or mobbing:
  [mobti.me](https://mobti.me/)
  or [agility timer](https://agility.jahed.dev/)

## Session Information

### Style & Duration

Any of the following formats will do:

- 2-hour [Prepared Kata](doc/PreparedKata.md)
- 2-hour [Randori in Pairs](doc/RandoriInPairs.md)
- 2-hour [Randori Kata](doc/RandoriKata.md)
- 2-hour [Mob Kata](doc/MobProgramming.md)

### Topic

Mixing top-down and bottom-up styles. This means starting with top-down, until we discover a brick that would be useful
and that we decide to build bottom-up. When the brick is advanced enough, we can plug it back in the main code and do
top-down again. We can then alternate a few times between both styles.

### Focus Points

- Early integration of the code
- Understanding of the difference between top-down and bottom-up
- Understanding of how to make the best of both styles

### Source Files

- [C++](cpp)
- [Go](go)
- [Java](java)
- [Python](python)
- [Typescript](typescript)

## License

`Kata-PascalTriangle` and the accompanying materials are made available
under the terms of the [MIT License](LICENSE.md) which accompanies this
distribution, and is available at the [Open Source site](https://opensource.org/licenses/MIT)

## Acknowledgements

See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md) for more information.

## Contributors

<table>
<tr>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/mengdaming>
            <img src=https://avatars.githubusercontent.com/u/1313765?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Damien Menanteau/>
            <br />
            <sub style="font-size:14px"><b>Damien Menanteau</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/philou>
            <img src=https://avatars.githubusercontent.com/u/23983?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Philippe Bourgau/>
            <br />
            <sub style="font-size:14px"><b>Philippe Bourgau</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/aatwi>
            <img src=https://avatars.githubusercontent.com/u/11088496?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=Ahmad Atwi/>
            <br />
            <sub style="font-size:14px"><b>Ahmad Atwi</b></sub>
        </a>
    </td>
    <td align="center" style="word-wrap: break-word; width: 150.0; height: 150.0">
        <a href=https://github.com/MirnaMx>
            <img src=https://avatars.githubusercontent.com/u/161314751?v=4 width="100;"  style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px" alt=MirnaMx/>
            <br />
            <sub style="font-size:14px"><b>MirnaMx</b></sub>
        </a>
    </td>
</tr>
</table>
