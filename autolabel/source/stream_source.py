#!/usr/bin/env python

# Copyright 2024 wheelos <daohu527@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import abc
import time
import cv2
from PIL import Image
from typing import Iterator, List


class StreamSource(metaclass=abc.ABCMeta):
    def __init__(self, interval: int):
        if interval <= 0:
            raise ValueError("Interval must be positive")
        self._interval = interval

    @abc.abstractmethod
    def __iter__(self) -> Iterator['StreamSource']:
        pass

    @abc.abstractmethod
    def __next__(self) -> object:
        pass

    @abc.abstractmethod
    def capture(self) -> Image.Image:
        pass

    @abc.abstractmethod
    def slice(self, duration: float) -> List[Image.Image]:
        pass

    @property
    def interval(self) -> int:
        return self._interval

    @interval.setter
    def interval(self, value: int):
        if value <= 0:
            raise ValueError("Interval must be positive")
        self._interval = value


class ScreenshotSource(StreamSource):
    def __init__(self, interval: int):
        super().__init__(interval)

    def capture(self) -> Image.Image:
        frame = cv2.cvtColor(cv2.imread(0), cv2.COLOR_BGR2RGB)
        return Image.fromarray(frame)

    def slice(self, duration: float) -> List[Image.Image]:
        """Capture screenshots for a specified duration, with each screenshot taken at self.interval."""
        screenshots = []
        end_time = time.time() + duration
        while time.time() < end_time:
            screenshots.append(self.capture())
            time.sleep(self.interval)
        return screenshots

    def __iter__(self) -> Iterator[Image.Image]:
        while True:
            yield self.capture()
            time.sleep(self.interval)

    def __next__(self) -> Image.Image:
        return self.capture()


class VideoSource(StreamSource):
    def __init__(self, interval: int):
        super().__init__(interval)

    def capture(self):
        pass

    def slice(self):
        """return video slice
        """
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


class VideoStreamSource(StreamSource):
    """webcam, stream and so on.
    """

    def __init__(self, interval: int):
        super().__init__(interval)

    def capture(self):
        pass

    def slice(self):
        """return video slice
        """
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass
