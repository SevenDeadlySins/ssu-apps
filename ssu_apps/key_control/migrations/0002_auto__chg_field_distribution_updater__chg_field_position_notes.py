# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Distribution.updater' to match new field type.
        db.rename_column(u'key_control_distribution', 'updater', 'updater_id')
        # Changing field 'Distribution.updater'
        db.alter_column(u'key_control_distribution', 'updater_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding index on 'Distribution', fields ['updater']
        db.create_index(u'key_control_distribution', ['updater_id'])


        # Changing field 'Position.notes'
        db.alter_column(u'key_control_position', 'notes', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Removing index on 'Distribution', fields ['updater']
        db.delete_index(u'key_control_distribution', ['updater_id'])


        # Renaming column for 'Distribution.updater' to match new field type.
        db.rename_column(u'key_control_distribution', 'updater_id', 'updater')
        # Changing field 'Distribution.updater'
        db.alter_column(u'key_control_distribution', 'updater', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Position.notes'
        db.alter_column(u'key_control_position', 'notes', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'updater': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
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