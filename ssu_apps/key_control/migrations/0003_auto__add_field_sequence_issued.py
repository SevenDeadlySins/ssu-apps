# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sequence.issued'
        db.add_column(u'key_control_sequence', 'issued',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sequence.issued'
        db.delete_column(u'key_control_sequence', 'issued')


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
            'sequence': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Sequence']"}),
            'transtype': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
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
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.KeyStatus']"})
        },
        u'key_control.sequence': {
            'Meta': {'unique_together': "(('position', 'sequence_num'),)", 'object_name': 'Sequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['key_control.Position']"}),
            'sequence_num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'key_control.usertype': {
            'Meta': {'object_name': 'UserType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usertype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['key_control']