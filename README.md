# Tamagotchi left/right game analyser

I love gen 1 pet, but the minigame is extremely frustrating. You'd like to have any control over wheter you win or not, but it's not clear what are you supposed to do to achieve that. I've heard a lot of conflicting theories. Some say it's completely random, 50% chance if you get left or right this time, others say you have to press the button in timing with tamagotchi's animation. Others say that there's a set of left-right combinations that is determined at the begining of the game, and yet others that there are combinations specific to certain characters, with mametchi knowing them all, and maskutchi the least.

Since many of those convictions might have originated in confirmation bias rooted in our desperation to feel at least a little bit in control, I set out to verify them in a scientific manner. However, keeping track of everything in a text editor became exhausting. At first I gave up, then I tried again, got exhausted again, and then I remembered I'm a programmer, so I quickly coded something that would do this job way easier. So here I am, bringing y'all my conclusions and a tool you may use if you want to test this for yourself.

## Methods
H0: All of 32 combinations are equally probable. Distribution is uniform and the chance to win by pressing only A button is 50%.

H1: Combinations are not equally probable. For certain character some set of combinations will never appear.

Binomial test was used for the final outcome (left or right winning), and Chi square test for distribution of combinations.

## Results

### Babytchi
<img width="612" height="513" alt="image" src="https://github.com/user-attachments/assets/321b9235-94bc-4691-a235-0be81e2cddb0" />

### Marutchi
<img width="581" height="487" alt="image" src="https://github.com/user-attachments/assets/d9bcbeaf-9661-4749-bef6-de300e72be4c" />

### Mametchi
<img width="618" height="489" alt="image" src="https://github.com/user-attachments/assets/a535133e-d758-4a86-a3e4-3403c048325a" />

### Maskutchi
<img width="580" height="488" alt="image" src="https://github.com/user-attachments/assets/0afe1c90-bb74-48ac-aa40-cf414bf0dd84" />

## Conclusions
Results were not statistically significant (p > 0.05) for whether pressing only left would guarantee winning for any of the tested characters. This means that just choosing your preffered button and sticking to it through the whole time gives you approximately 50% chance to win any game.

As for distribution, results were significant only for Marutchi and Maskutchi. But the notion that some of the characters have only certain amount of combinations remembered wasn't confirmed - after enough games all or almost all combinations always appeared at least once. Since result was statistically significant only for two of the characters and it's unlikely that programmers implemented very complex probability system instead of just 50% chance for each direction, I think it's safe to assume that it was just a result of chance. It may be due to pseudorandomness of the computer generated results - they are based on the clock, so it's possible that I got into a certain rythm of clicking the button that made some combinations more probable than others. But I didn't test for the effect of clicking in sync with tamagotchi's animations, so this may be possible explanation as well.

I didn't analise the order of the combinations, but at the first glance there doesn't seem to be any pattern in which they follow after each other. 

**All in all, it seems the most logical to conclude that, unfortunately, it is just 50% chance for getting left or right at any given time, although possibility of tamagotchi's movement at the time of click or other factor influencing the result cannot be exluded.**

## Limitations
A very huge limitation is a mistake I made in code, not realising that Python does, in fact, treat 0 as equal to False. This caused left-only combinations to not be registered at all for Maskutchi, Babytchi and Marutchi until I fixed it (Mametchi was unaffected, since their data was not inputter through the program). But given the results we already have, I don't think it would change much, and I am not doing it all over again.

Another limitation is the fact that I sometimes played with my tama to fill their hearts without registering the results I got, and the possibility that I could do some mistakes in typing (that was a lot of typing), although I always tried to confirm with the amount of wins and loses I got at the end of each game.

## How to use it
First, you need to download Python 3.14.3 or newest. Then download or clone the repository, start the "run.bat" file and follow the instructions from there. Remember to save before you close the window! 
