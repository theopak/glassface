# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GlassfaceUser.profile_picture1'
        db.add_column(u'glassface_glassfaceuser', 'profile_picture1',
                      self.gf('django_filepicker.models.FPFileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'GlassfaceUser.profile_picture2'
        db.add_column(u'glassface_glassfaceuser', 'profile_picture2',
                      self.gf('django_filepicker.models.FPFileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'GlassfaceUser.profile_picture3'
        db.add_column(u'glassface_glassfaceuser', 'profile_picture3',
                      self.gf('django_filepicker.models.FPFileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'GlassfaceUser.profile_picture4'
        db.add_column(u'glassface_glassfaceuser', 'profile_picture4',
                      self.gf('django_filepicker.models.FPFileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'GlassfaceUser.profile_picture5'
        db.add_column(u'glassface_glassfaceuser', 'profile_picture5',
                      self.gf('django_filepicker.models.FPFileField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'GlassfaceUser.facebook_id'
        db.add_column(u'glassface_glassfaceuser', 'facebook_id',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


        # Changing field 'GlassfaceUser.facebook_pass'
        db.alter_column(u'glassface_glassfaceuser', 'facebook_pass', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'GlassfaceUser.facebook_email'
        db.alter_column(u'glassface_glassfaceuser', 'facebook_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'GlassfaceUser.profile_picture1'
        db.delete_column(u'glassface_glassfaceuser', 'profile_picture1')

        # Deleting field 'GlassfaceUser.profile_picture2'
        db.delete_column(u'glassface_glassfaceuser', 'profile_picture2')

        # Deleting field 'GlassfaceUser.profile_picture3'
        db.delete_column(u'glassface_glassfaceuser', 'profile_picture3')

        # Deleting field 'GlassfaceUser.profile_picture4'
        db.delete_column(u'glassface_glassfaceuser', 'profile_picture4')

        # Deleting field 'GlassfaceUser.profile_picture5'
        db.delete_column(u'glassface_glassfaceuser', 'profile_picture5')

        # Deleting field 'GlassfaceUser.facebook_id'
        db.delete_column(u'glassface_glassfaceuser', 'facebook_id')


        # Changing field 'GlassfaceUser.facebook_pass'
        db.alter_column(u'glassface_glassfaceuser', 'facebook_pass', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'GlassfaceUser.facebook_email'
        db.alter_column(u'glassface_glassfaceuser', 'facebook_email', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

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
        u'glassface.glassfaceuser': {
            'Meta': {'object_name': 'GlassfaceUser'},
            'facebook_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facebook_pass': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_picture': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'profile_picture1': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'profile_picture2': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'profile_picture3': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'profile_picture4': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'profile_picture5': ('django_filepicker.models.FPFileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['glassface']