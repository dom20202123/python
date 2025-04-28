class Television():
        '''
        Sets up the maximum and minimum values for volume for the channel
        MIN_VOLUME: sets up the minimum value for volume
        MAX_VOLUME: sets up the maximum value for volume
        MIN_CHANNEL: sets up the minimum value for channels
        MAX_CHANNEL: sets up the maximum value for channels
        '''
        MIN_VOLUME : int = 0
        MAX_VOLUME: int = 2
        MIN_CHANNEL : int = 0
        MAX_CHANNEL: int = 3
        def __init__(self) -> None:
            '''
            Sets up the values for what the volume, channel, status, and muted are
            self.__status: Controls whether the TV is on or not, if its false its off, if True its on
            self.__muted : Controls whether the TV is muted or not, if its false its unmuted, if True its muted
            self.__volume: Controls the current volume for the tv
            self.__channel: Controls the current channel for the tv
            '''
            self.__status : bool = False
            self.__muted : bool = False
            self.__volume : int = Television.MIN_VOLUME
            self.__channel: int = Television.MIN_CHANNEL

        def power(self) -> None:
            '''Changes self.__status to false or true which controls if the tv is on or off '''
            if True == self.__status:
                self.__status = False
            elif False == self.__status:
                self.__status = True

        def mute(self) -> None:
            '''Controls self.__muted to false or true which controls if the tv is muted or unmuted'''
            if True == self.__status:
                if True == self.__muted:
                    self.__muted = False
                elif False == self.__muted:(
                    self.__muted) = True

        def channel_up(self) -> None:
            '''Changes the channel of the TV when on and channels are going up
            If the channel is the same as the max channel it resets back to the value of the minimum
            '''
            if self.__status == True:
                self.__channel += 1
                if  self.__channel > Television.MAX_CHANNEL:
                    self.__channel = Television.MIN_CHANNEL

        def channel_down(self) -> None:
            '''Changes the channel of the TV when on and channels are going down
            If the channel is the same as the min channel it resets back to the value of the maximum
            '''
            if self.__status == True:
                self.__channel -= 1
                if  self.__channel < Television.MIN_CHANNEL:
                    self.__channel = Television.MAX_CHANNEL

        def volume_up(self) -> None:
            '''Controls the volume of the tv when it's going up if the tv is on
            If the TV is at the maximum though at this function is called it doesn't increase and stays at the maximum value'''
            if self.__status == True:
                self.__muted = False
                self.__volume += 1
                if self.__volume >= Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME

        def volume_down(self) -> None:
            '''Controls the volume of the tv when it's going down if the tv is on
            If the TV is at the minimum though at this function is called it doesn't decrease so it stays at the minimum value'''
            if self.__status == True:
                self.__muted = False
                self.__volume -= 1
                if self.__volume <= Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME



        def __str__(self) -> str:
            '''Returns the status of the tv
            return: tv status'''
            if self.__muted == False:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
            elif self.__muted == True:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'

