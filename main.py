import os
import interactions


TOKEN = os.environ.get("TOKEN")

bot = interactions.Client()

@interactions.listen()
async def on_startup():
    print("Bot is ready!")

@interactions.slash_command(name="hellof", description="Says hello to a user")
async def say_hello(ctx):
    await ctx.send("Hello! " + ctx.author.username)

"""
@interactions.slash_command(
    name="base",
    description="My command base",
    group_name="group",
    group_description="My command group",
    sub_cmd_name="command",
    sub_cmd_description="My command",
)
async def my_command_function(ctx: interactions.InteractionContext):
    await ctx.send("Hello World")

@my_command_function.subcommand(sub_cmd_name="second_command", sub_cmd_description="My second command")
async def my_second_command_function(ctx: interactions.InteractionContext):
    await ctx.send("Hello World")
"""

#Command count users in server
@interactions.slash_command(name="count", description="Count users in server")
async def count(ctx):
    total = ctx.guild.member_count
    await ctx.send(embed=interactions.Embed(title="Count users in server :", description="Humans : " + str(len(ctx.guild.members)) + "/" + str(total) 
    + "\nBots : " + str(total - len(ctx.guild.members)) + "/" + str(total), color=interactions.Color.from_rgb(255, 0, 0)))


bot.start(TOKEN)
