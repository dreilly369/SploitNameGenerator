#!/usr/bin/env python2
#encoding: UTF-8
from os import path
import sys
from random import randint

class NameGenerator:
    root_dir = path.dirname(path.abspath(__file__))
    bad_chars = ["\'","`",","]
    verb_dir = root_dir + "/verbs/"
    adverb_dir = root_dir + "/adverbs/"
    adjective_dir = root_dir + "/adjectives/"
    noun_dir = root_dir + "/nouns/"
    # generate some random names

    def gen_phrase(self, path_1, path_2):
        adjs = []
        nouns = []
        with open(path_1, 'r') as f:
            adjs = f.read().strip().splitlines()
            f.close()
        with open(path_2, 'r') as f:
            nouns = f.read().strip().splitlines()
            f.close()
        adj_i = randint(0, len(adjs))
        noun_i = randint(0, len(nouns))

        adj = adjs[adj_i]
        noun = nouns[noun_i]
        s = "%s %s" % (adj, noun)
        return s

    def gen_adjnoun(self):
        f1 = "%s/28Kadjectives.txt" % self.adjective_dir
        f2 = "%s/91Knouns.txt" % self.noun_dir
        name = self.gen_phrase(f1, f2)
        return name.title()

    def gen_adjverb(self):
        f1 = "%s/28Kadjectives.txt" % self.adjective_dir
        f2 = "%s/31Kverbs.txt" % self.verb_dir
        name = self.gen_phrase(f1, f2)
        return name.title()

    def gen_advbnoun(self):
        f1 = "%s/6Kadverbs.txt" % self.adverb_dir
        f2 = "%s/91Knouns.txt" % self.noun_dir
        name = self.gen_phrase(f1, f2)
        return name.title()

    def gen_verbnoun(self):
        f1 = "%s/31Kverbs.txt" % self.verb_dir
        f2 = "%s/91Knouns.txt" % self.noun_dir
        name = self.gen_phrase(f1, f2)
        return name.title()

if __name__ == "__main__":
    try:
        gen_amt = int(sys.argv[1])
        if gen_amt > 100:
            print "Limiting Generation to 100"
            gen_amt = 100
        elif gen_amt < 1:
            print "Need at least 1 to test generator"
            exit()
    except:
        print "Defaulting to 10 names"
        gen_amt = 10
    try:
        gen_type = sys.argv[2]
        types = ["advbnoun","verbnoun","adjverb","adjnoun"]
        if gen_type.lower() not in types:
            print "\n".join(types)
            print "please select a type from the list."
            exit()
    except:
        print "Defaulting to adjnoun"
        gen_type = "adjnoun"
    ng = NameGenerator()
    func = "ng.gen_%s()" % gen_type.lower()
    print "=" * 30
    for i in range(0,gen_amt+1):
        print eval(func)
    print "=" * 30