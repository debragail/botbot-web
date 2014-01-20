# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ChatBot'
        db.create_table(u'bots_chatbot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('connection', self.gf('django_hstore.fields.DictionaryField')(default={'is': 'not used'}, db_index=True)),
            ('server', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('server_password', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('real_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'bots', ['ChatBot'])

        # Adding model 'Channel'
        db.create_table(u'bots_channel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('chatbot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bots.ChatBot'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'bots', ['Channel'])

        # Adding model 'UserCount'
        db.create_table(u'bots_usercount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bots.Channel'])),
            ('dt', self.gf('django.db.models.fields.DateField')()),
            ('counts', self.gf('djorm_pgarray.fields.ArrayField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'bots', ['UserCount'])


    def backwards(self, orm):
        # Deleting model 'ChatBot'
        db.delete_table(u'bots_chatbot')

        # Deleting model 'Channel'
        db.delete_table(u'bots_channel')

        # Deleting model 'UserCount'
        db.delete_table(u'bots_usercount')


    models = {
        u'accounts.membership': {
            'Meta': {'unique_together': "(('user', 'channel'),)", 'object_name': 'Membership'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bots.Channel']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_owner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.User']"})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User', 'db_table': "'auth_user'"},
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
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        u'bots.channel': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Channel'},
            'chatbot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bots.ChatBot']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'plugins': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plugins.Plugin']", 'through': u"orm['plugins.ActivePlugin']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['accounts.User']", 'through': u"orm['accounts.Membership']", 'symmetrical': 'False'})
        },
        u'bots.chatbot': {
            'Meta': {'object_name': 'ChatBot'},
            'connection': ('django_hstore.fields.DictionaryField', [], {'default': "{'is': 'not used'}", 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'real_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'server': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'server_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'bots.usercount': {
            'Meta': {'object_name': 'UserCount'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bots.Channel']"}),
            'counts': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dt': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'plugins.activeplugin': {
            'Meta': {'object_name': 'ActivePlugin'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bots.Channel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['plugins.Plugin']"}),
            'variables': ('django_hstore.fields.DictionaryField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'plugins.plugin': {
            'Meta': {'object_name': 'Plugin'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['bots']