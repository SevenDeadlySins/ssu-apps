# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserType'
        db.create_table(u'key_control_usertype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usertype', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'key_control', ['UserType'])

        # Adding model 'KeyType'
        db.create_table(u'key_control_keytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('keytype', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'key_control', ['KeyType'])

        # Adding model 'KeyStatus'
        db.create_table(u'key_control_keystatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'key_control', ['KeyStatus'])

        # Adding model 'Position'
        db.create_table(u'key_control_position', (
            ('position', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('keytype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.KeyType'])),
            ('keyway', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.KeyStatus'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'key_control', ['Position'])

        # Adding model 'Sequence'
        db.create_table(u'key_control_sequence', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.Position'])),
        ))
        db.send_create_signal(u'key_control', ['Sequence'])

        # Adding model 'Distribution'
        db.create_table(u'key_control_distribution', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.Position'])),
            ('sequence', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.Sequence'])),
            ('transtype', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('updater', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('usertype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.UserType'])),
            ('userID', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('department', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('duedate', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'key_control', ['Distribution'])

        # Adding model 'Location'
        db.create_table(u'key_control_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['key_control.Position'])),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('propnum', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'key_control', ['Location'])


    def backwards(self, orm):
        # Deleting model 'UserType'
        db.delete_table(u'key_control_usertype')

        # Deleting model 'KeyType'
        db.delete_table(u'key_control_keytype')

        # Deleting model 'KeyStatus'
        db.delete_table(u'key_control_keystatus')

        # Deleting model 'Position'
        db.delete_table(u'key_control_position')

        # Deleting model 'Sequence'
        db.delete_table(u'key_control_sequence')

        # Deleting model 'Distribution'
        db.delete_table(u'key_control_distribution')

        # Deleting model 'Location'
        db.delete_table(u'key_control_location')


    models = {
        u'key_control.distribution': {
            'Meta': {'object_name': 'Distribution'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'duedate': ('django.db.models.fields.DateField', [], {}),
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Position']"}),
            'sequence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Sequence']"}),
            'transtype': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'updater': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'userID': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'usertype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.UserType']"})
        },
        u'key_control.keystatus': {
            'Meta': {'object_name': 'KeyStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'key_control.keytype': {
            'Meta': {'object_name': 'KeyType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keytype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'key_control.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Position']"}),
            'propnum': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'key_control.position': {
            'Meta': {'object_name': 'Position'},
            'keytype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.KeyType']"}),
            'keyway': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'position': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.KeyStatus']"})
        },
        u'key_control.sequence': {
            'Meta': {'object_name': 'Sequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Position']"})
        },
        u'key_control.usertype': {
            'Meta': {'object_name': 'UserType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usertype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['key_control']