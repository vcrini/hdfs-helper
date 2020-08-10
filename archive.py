#!/usr/bin/env python3

import argparse
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument('--date', required=True)
parser.add_argument('--path', required=True)

args = parser.parse_args()
tm = Template("""
hadoop archive -Dmapreduce.map.memory.mb=8192 -Dmapreduce.reduce.memory.mb=8192 -Dmapred.child.java.opts=-Xmx8192m -Dyarn.app.mapreduce.am.resource.mb=4096 -archiveName {{date}}.har -p {{path}}/{{date}} {{path}}
""")
command = []
for path in args.path.split(","):
    msg = tm.render(date=args.date, path=path)
    command.append(msg)
print(" && ".join(command))

# Hello,
# {% if action == 'rm'  %}
# initial situation:
# {% for name in names %}
# kafka-topics --zookeeper {{ environment }} --describe --topic {{ name }} 2>/dev/null |grep -v CLASSPATH
# kafka-sentry -lp -r {{ role }} 2>/dev/null|grep -v CLASSPATH|grep ={{ name }}
# {% endfor %}
# {% endif %}
#
# {{ comment }}
# {% for name in names %}
# {% if action == 'rm'  %}
# kafka-topics --zookeeper {{ environment }} --delete --topic {{ name }} 2>/dev/null |grep -v CLASSPATH
# {% else  %}
# kafka-topics --zookeeper {{ environment }} --create --partitions 1 --replication-factor 3  --topic {{ name }}  2>/dev/null |grep -v CLASSPATH
# {% endif %}
# kafka-sentry -{{ act }}pr -r {{ role }} -p 'TOPIC={{ name }}->action=describe'
# kafka-sentry -{{ act }}pr -r {{ role }} -p 'TOPIC={{ name }}->action=read'
# kafka-sentry -{{ act }}pr -r {{ role }} -p 'TOPIC={{ name }}->action=write'
# {% endfor %}
# results
#
# {% for name in names %}
# kafka-topics --zookeeper {{ environment }} --describe --topic {{ name }} 2>/dev/null |grep -v CLASSPATH
# kafka-sentry -lp -r {{ role }} 2>/dev/null|grep -v CLASSPATH|grep ={{ name }}
#
# {% endfor %}
# """)
# if args.group:
#     tm = Template("""
# Hello,
# {% if action == 'rm'  %}
# initial situation:
# {% for name in names %}
# kafka-sentry -lp -r {{ role }} 2>/dev/null|grep -v CLASSPATH|grep ={{ name }}
# {% endfor %}
# {% endif %}
# {{ comment }}
# {% for name in names %}
# kafka-sentry -{{ act }}pr -r {{ role }} -p 'HOST=*->CONSUMERGROUP={{ name }}->action=describe'
# kafka-sentry -{{ act }}pr -r {{ role }} -p 'HOST=*->CONSUMERGROUP={{ name }}->action=read'
# {% endfor %}
# results:
#
# {% for name in names %}
# kafka-sentry -lp -r {{ role }} 2>/dev/null|grep -v CLASSPATH|grep ={{ name }}
# {% endfor %}
# """)
#
#
# msg = tm.render(action=args.action, act=act[args.action], comment=comment[args.profile],
#                 environment=environment[args.profile], names=args.name.split(","), role=args.role)
# print(msg)
