# Import packages
import nltk
nltk.download('punkt')

# Store a paragraph
paragraph = '''What this handout is about. This handout will help you create an effective speech by establishing the purpose of your speech and making it easily understandable.
It will also help you to analyze your audience and keep the audience interested. What’s different about a speech? Writing for public speaking isn’t so different from other types of writing. You want to engage your audience’s attention, convey your ideas in a logical manner and use reliable evidence to support your point. But the conditions for public speaking favor some writing qualities over others.
 When you write a speech, your audience is made up of listeners. They have only one chance to comprehend the information as you read it, so your speech must be well-organized and easily understood. In addition, the content of the speech and your delivery must fit the audience. What’s your purpose? People have gathered to hear you speak on a specific issue, and they expect to get something out of it immediately. And you, the speaker, hope to have an immediate effect on your audience. The purpose of your speech is to get the response you want. Most speeches invite audiences to react in one of three ways: feeling, thinking, or acting. For example, eulogies encourage emotional response from the audience; college lectures stimulate listeners to think about a topic from a different perspective; protest speeches in the Pit recommend actions the audience can take.
As you establish your purpose, ask yourself these questions: What do you want the audience to learn or do? If you are making an argument, why do you want them to agree with you? If they already agree with you, why are you giving the speech? How can your audience benefit from what you have to say? Audience analysis If your purpose is to get a certain response from your audience, you must consider who they are (or who you’re pretending they are). If you can identify ways to connect with your listeners, you can make your speech interesting and useful. As you think of ways to appeal to your audience, ask yourself: What do they have in common? Age? Interests? Ethnicity? Gender? Do they know as much about your topic as you, or will you be introducing them to new ideas? Why are these people listening to you? What are they looking for? What level of detail will be effective for them? What tone will be most effective in conveying your message? What might offend or alienate them? For more help, see our handout on audience. Creating an effective introduction Get their attention, otherwise known as “The Hook”. Think about how you can relate to these listeners and get them to relate to you or your topic. Appealing to your audience on a personal level captures their attention and concern, increasing the chances of a successful speech. Speakers often begin with anecdotes to hook their audience’s attention. Other methods include presenting shocking statistics, asking direct questions of the audience, or enlisting audience participation.
Establish context and/or motive. Explain why your topic is important. Consider your purpose and how you came to speak to this audience. You may also want to connect the material to related or larger issues as well, especially those that may be important to your audience. Get to the point. Tell your listeners your thesis right away and explain how you will support it. Don’t spend as much time developing your introductory paragraph and leading up to the thesis statement as you would in a research paper for a course. Moving from the intro into the body of the speech quickly will help keep your audience interested. You may be tempted to create suspense by keeping the audience guessing about your thesis until the end, then springing the implications of your discussion on them. But if you do so, they will most likely become bored or confused. For more help, see our handout on introductions. Making your speech easy to understand.Repeat crucial points and buzzwords Especially in longer speeches, it’s a good idea to keep reminding your audience of the main points you’ve made. For example, you could link an earlier main point or key term as you transition into or wrap up a new point. You could also address the relationship between earlier points and new points through discussion within a body paragraph. Using buzzwords or key terms throughout your paper is also a good idea. If your thesis says you’re going to expose unethical behavior of medical insurance companies, make sure the use of “ethics” recurs instead of switching to “immoral” or simply “wrong.” Repetition of key terms makes it easier for your audience to take in and connect information.'''

# Tokenize sentenses and words
sentence = nltk.sent_tokenize(paragraph)
word = nltk.word_tokenize(paragraph)

#List of sentences in the paragraph
print("List of the sentences in the paragraph are :\n")
sentence

print("Number of sentences in the paragraph =",len(sentence))

#List of words in the paragraph
print("List of the words in the paragraph are :\n")
word

print("Total number of words in the paragraph =",len(word))
