import Randomiser
import asyncio

randomizer = Randomiser.MusicPlayer()

commands = {
    "n": "randomizer.PlayNext()",
    "p": "randomizer.Pause()",
    "c": "print(randomizer.GetMusicName())",
    "v": "print(randomizer.GetVolume())"
}


async def Update():
    while True:
        randomizer.Update()

        await asyncio.sleep(5)


async def Inputs():
    while True:
        command = await asyncio.to_thread(input, 'Enter the command: ')

        if 'v_' in command:
            volume = float(command.split('_')[len(command.split('_')) - 1])
            randomizer.SetVolume(volume)
        else:
            for letter in command:
                try:
                    exec(commands[letter.lower()])
                    await asyncio.sleep(0.2)
                except KeyError:
                    pass

        print()


async def main():
    randomizer.SetVolume(100)

    print('You can use some commands in one (for example cncpp)\n' +
          'n (next): next song\nc (current): name of the current song\n' +
          'p (pause): make pause/unpause\nv (get volume): get music volume\n' +
          'v_value (v_2, v_100 etc.): sets the music volume. Value cannot be more than 100 and less than 0.' +
          " Do not use with others commands\n")

    print(randomizer.GetMusicName() + ' is playing now\n')

    task1 = asyncio.create_task(Inputs())
    task2 = asyncio.create_task(Update())

    await asyncio.gather(task1, task2)


asyncio.run(main())
