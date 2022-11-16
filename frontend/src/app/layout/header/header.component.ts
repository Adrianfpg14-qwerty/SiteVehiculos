import { Component, OnInit } from '@angular/core';
import { MenuItem } from 'primeng/api';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css'],
})
export class HeaderComponent implements OnInit {
  opc: MenuItem[] = [];
  estilosMenu: {} = {
    'background-color': '#8DC3D8',
    border: '0',
    padding: '0px 0px 0px 0px',
  };
  constructor() {}

  ngOnInit(): void {
    this.opc = [
    // items: [
      //   {
      //     label: 'Crud Cliente'
      //   },
      //   {
      //     label: 'HTML 2'
      //   }
      // ]
      {
        label: 'Personas',
        icon: 'pi pi-fw pi-users',
        routerLink: '/personas',
      },
      {
        label: 'Multas',
        icon: 'pi pi-fw pi-qrcode',
        routerLink: '/multas',
      },
      {
        label: 'Vehiculos',
        icon: 'pi pi-fw pi-shopping-cart',
        routerLink: '/vehiculos',
      },
    ];
  }
}
