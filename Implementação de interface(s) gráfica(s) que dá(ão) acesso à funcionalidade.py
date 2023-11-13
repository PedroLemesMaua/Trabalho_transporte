import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'edit-route',
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('edit-route'),
      ),
      body: Center(
        child: Text('import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditRouteComponent } from './edit-route.component';

describe('EditRouteComponent', () => {
  let component: EditRouteComponent;
  let fixture: ComponentFixture<EditRouteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditRouteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditRouteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
'),
      ),
    );
  }
}


#!/bin/bash

# Obtém o nome do repositório
repo_name=$(git remote get-url origin | sed -E 's/.*github.com\/(.*)\/.*/\1/')

# Obtém o nome da release
release_name=$(date +"%Y-%m-%d")

# Cria a release
git tag -a $release_name -m "Release $release_name"

# Adiciona o código da interface gráfica
git add ./frontend/src

# Commita as alterações
git commit -m "Adiciona a implementação da interface gráfica"

# Pusha as alterações para o repositório
git push origin $release_name
