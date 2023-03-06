import logging

from config import *
from git import Repo
from pyShicy import PyrogramXd
from pyShicy.Clients import *
from pyShicy.config import Var
from pyShicy.pyrogram import eod, eor


repo = Repo()
branch = repo.active_branch
chiy = PyrogramXd()
var = Var()
hndlr = [
    f"{var.HNDLR[0]}",
    f"{var.HNDLR[1]}",
    f"{var.HNDLR[2]}",
    f"{var.HNDLR[3]}",
    f"{var.HNDLR[4]}",
    f"{var.HNDLR[5]}",
]
logs = logging.getLogger(__name__)
