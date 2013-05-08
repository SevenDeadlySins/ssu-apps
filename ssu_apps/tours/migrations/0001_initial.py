# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tour'
        db.create_table(u'tours_tour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tour_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tour_count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tours', ['Tour'])


    def backwards(self, orm):
        # Deleting model 'Tour'
        db.delete_table(u'tours_tour')


    models = {
        u'tours.tour': {
            'Meta': {'object_name': 'Tour'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tour_count': ('django.db.models.fields.IntegerField', [], {}),
            'tour_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['tours']